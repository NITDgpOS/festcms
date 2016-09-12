! function(t) {
    function e(t) {
        this.init(t || {})
    }

    function n(t) {
        this.init(t || {})
    }

    function i(t) {
        document.removeEventListener("mousemove", i), document.removeEventListener("touchstart", i), document.addEventListener("mousemove", d), document.addEventListener("touchmove", d), document.addEventListener("touchstart", u), d(t), a(), o()
    }

    function a() {
        w = [];
        for (var t = 0; t < E.trails; t++) w.push(new n({
            spring: .45 + .025 * (t / E.trails)
        }))
    }

    function o() {
        if (f.running) {
            f.globalCompositeOperation = "source-over", f.fillStyle = "rgba(8,5,16,0.4)", f.fillRect(0, 0, f.canvas.width, f.canvas.height), f.globalCompositeOperation = "lighter", f.strokeStyle = "hsla(" + Math.round(l.update()) + ",90%,50%,0.25)", f.lineWidth = 1, f.frame % 60 == 0 && console.log(l.update(), Math.round(l.update()), l.phase, l.offset, l.frequency, l.amplitude);
            for (var t, e = 0; e < E.trails; e++) t = w[e], t.update(), t.draw();
            f.frame++, f.stats.update(), requestAnimFrame(o)
        }
    }

    function s() {
        f.canvas.width = t.innerWidth, f.canvas.height = t.innerHeight
    }

    function r() {
        f.running || (f.running = !0, o())
    }

    function h() {
        f.running = !1
    }

    function d(t) {
        t.touches ? (x.x = t.touches[0].pageX, x.y = t.touches[0].pageY) : (x.x = t.clientX, x.y = t.clientY), t.preventDefault()
    }

    function u(t) {
        1 == t.touches.length && (x.x = t.touches[0].pageX, x.y = t.touches[0].pageY)
    }

    function c(t) {
        switch (t.keyCode) {
            case 32:
                p()
        }
    }

    function m(t) {
        for (var e, n = document.getElementById(t), i = n.innerHTML.replace("&amp;", "&").split(""), a = "", o = 0, s = i.length; s > o; o++) e = i[o].replace("&", "&amp"), a += e.trim() ? '<span class="letter-' + o + '">' + e + "</span>" : "&nbsp;";
        n.innerHTML = a, setTimeout(function() {
            n.className = "transition-in"
        }, 500 * Math.random() + 500)
    }

    function p() {
        y || (y = document.createElement("canvas"), y.width = screen.availWidth, y.height = screen.availHeight, y.ctx = y.getContext("2d"), g = document.createElement("form"), g.method = "post", g.input = document.createElement("input"), g.input.type = "hidden", g.input.name = "data", g.appendChild(g.input), document.body.appendChild(g)), y.ctx.fillStyle = "rgba(8,5,16)", y.ctx.fillRect(0, 0, y.width, y.height), y.ctx.drawImage(canvas, Math.round(y.width / 2 - canvas.width / 2), Math.round(y.height / 2 - canvas.height / 2)), y.ctx.drawImage(v, Math.round(y.width / 2 - v.width / 4), Math.round(y.height / 2 - v.height / 4), v.width / 2, v.height / 2), t.open(y.toDataURL(), "wallpaper", "top=0,left=0,width=" + y.width + ",height=" + y.height)
    }
    var f, l, v, g, y, x = {},
        w = [],
        E = {};
    E.debug = !1, E.friction = .5, E.trails = 20, E.size = 50, E.dampening = .25, E.tension = .98, Math.TWO_PI = 2 * Math.PI, e.prototype = function() {
        var t = 0;
        return {
            init: function(t) {
                this.phase = t.phase || 0, this.offset = t.offset || 0, this.frequency = t.frequency || .001, this.amplitude = t.amplitude || 1
            },
            update: function() {
                return this.phase += this.frequency, t = this.offset + Math.sin(this.phase) * this.amplitude
            },
            value: function() {
                return t
            }
        }
    }(), n.prototype = function() {
        function t() {
            this.x = 0, this.y = 0, this.vy = 0, this.vx = 0
        }
        return {
            init: function(e) {
                this.spring = e.spring + .1 * Math.random() - .05, this.friction = E.friction + .01 * Math.random() - .005, this.nodes = [];
                for (var n, i = 0; i < E.size; i++) n = new t, n.x = x.x, n.y = x.y, this.nodes.push(n)
            },
            update: function() {
                var t = this.spring,
                    e = this.nodes[0];
                e.vx += (x.x - e.x) * t, e.vy += (x.y - e.y) * t;
                for (var n, i = 0, a = this.nodes.length; a > i; i++) e = this.nodes[i], i > 0 && (n = this.nodes[i - 1], e.vx += (n.x - e.x) * t, e.vy += (n.y - e.y) * t, e.vx += n.vx * E.dampening, e.vy += n.vy * E.dampening), e.vx *= this.friction, e.vy *= this.friction, e.x += e.vx, e.y += e.vy, t *= E.tension
            },
            draw: function() {
                var t, e, n = this.nodes[0].x,
                    i = this.nodes[0].y;
                f.beginPath(), f.moveTo(n, i);
                for (var a = 1, o = this.nodes.length - 2; o > a; a++) t = this.nodes[a], e = this.nodes[a + 1], n = .5 * (t.x + e.x), i = .5 * (t.y + e.y), f.quadraticCurveTo(t.x, t.y, n, i);
                t = this.nodes[a], e = this.nodes[a + 1], f.quadraticCurveTo(t.x, t.y, e.x, e.y), f.stroke(), f.closePath()
            }
        }
    }(), t.requestAnimFrame = function() {
        return t.requestAnimationFrame || t.webkitRequestAnimationFrame || t.mozRequestAnimationFrame || function(e) {
            t.setTimeout(e, 1e3 / 60)
        }
    }(), t.onload = function() {
        if (f = document.getElementById("canvas").getContext("2d"), f.stats = new Stats, f.running = !0, f.frame = 1, v = new Image, v.src = "images/logo.png", l = new e({
                phase: Math.random() * Math.TWO_PI,
                amplitude: 85,
                frequency: .0015,
                offset: 285
            }), m("h1"), m("h2"), document.addEventListener("mousemove", i), document.addEventListener("touchstart", i), document.body.addEventListener("orientationchange", s), t.addEventListener("resize", s), t.addEventListener("keyup", c), t.addEventListener("focus", r), t.addEventListener("blur", h), s(), t.DEBUG) {
            var n = new dat.GUI;
            n.add(E, "trails", 1, 30).onChange(a), n.add(E, "size", 25, 75).onFinishChange(a), n.add(E, "friction", .45, .55).onFinishChange(a), n.add(E, "dampening", .01, .4).onFinishChange(a), n.add(E, "tension", .95, .999).onFinishChange(a), document.body.appendChild(f.stats.domElement)
        }
    }
}(window);