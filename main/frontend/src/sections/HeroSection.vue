<template>
  <section id="hero">
    <div class="hero-main">
      <div class="hero-left">
        <p class="hero-kicker">Cybersecurity Portfolio · 2025</p>
        <h1 class="hero-h1">
          Jan.<br>
          <span class="pink">Sultan</span><br>
          <span class="ghost">Cybersecurity</span>
        </h1>
        <p class="hero-p">
          Aspiring <strong>penetration tester</strong>.
          I pull things apart to understand how they work — then build them better.
        </p>
        <div class="hero-cta">
          <a href="#projects" class="btn btn-pri">View Projects</a>
          <a href="#guestbook" class="btn btn-ghost">Sign Guestbook</a>
        </div>
      </div>
      <div class="hero-right">
        <TerminalBlock />
        <HeroMeta />
      </div>
    </div>
  </section>
</template>

<script setup>
import TerminalBlock from './TerminalBlock.vue'
import HeroMeta from './HeroMeta.vue'
</script>

<style scoped>
#hero{
  position:relative;z-index:1;
  min-height:100vh;
  display:grid;
  grid-template-rows:1fr auto;
  padding:0;
}
.hero-main{
  display:grid;
  grid-template-columns:1fr 1fr;
  align-items:center;
  max-width:1100px;margin:0 auto;width:100%;
  padding:100px clamp(1.5rem,6vw,5rem) 4rem;
  gap:4rem;
}
.hero-kicker{
  font-family:var(--mono);font-size:10px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--pink);
  margin-bottom:1.75rem;
  display:flex;align-items:center;gap:.75rem;
  animation:fadeUp .5s .2s forwards;
}
.hero-kicker::before{content:'';width:28px;height:1px;background:var(--pink);}
.hero-h1{
  font-family:var(--serif);
  font-size:clamp(3.5rem,7vw,5.8rem);
  line-height:.93;font-weight:900;
  color:var(--white);
  margin-bottom:1.75rem;
  animation:fadeUp .7s .35s forwards;
}
.hero-h1 span.pink{color:var(--pink);}
.hero-h1 span.italic{font-style:italic;color:var(--pink-pale);}
.hero-h1 span.ghost{
  -webkit-text-stroke:1.5px var(--rule2);
  color:transparent;
}
.hero-p{
  font-size:15px;color:var(--muted);font-weight:300;
  max-width:420px;line-height:1.75;
  margin-bottom:2.5rem;
  animation:fadeUp .7s .5s forwards;
}
.hero-p strong{color:var(--pink);font-weight:500;}
.hero-cta{
  display:flex;gap:.85rem;flex-wrap:wrap;
  animation:fadeUp .6s .65s forwards;
}
.hero-right{
  animation:fadeUp .8s .55s both;
  display:flex;flex-direction:column;gap:1.25rem;
  align-self:center;
}
@media(max-width:860px){
  .hero-main{grid-template-columns:1fr;gap:2.5rem;}
  .hero-right{display:none;}
}
</style>