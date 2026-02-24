<template>
  <div class="photo-block">
    <div class="photo-frame">
      <img 
        src="../assets/profile.jpg"
        alt="Jan Sultan" 
        class="photo-img"
      >
    </div>
    <div class="photo-meta">
      <div class="photo-name">Jan Sultan</div>
      <div class="photo-role">Student · Aspiring Pentester</div>
    </div>
  </div>
</template>

<style scoped>
.photo-block {
  margin-bottom: 1.25rem;
}

.photo-frame {
  width: 100%;
  aspect-ratio: 1/1;
  background: var(--ink2);
  border: 1px solid var(--rule2);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.photo-frame::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(244,167,185,0.1) 0%, transparent 50%);
  pointer-events: none;
  z-index: 1;
}

.photo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: grayscale(20%) contrast(1.05);
  transition: filter 0.3s ease, transform 0.3s ease;
}

.photo-frame:hover .photo-img {
  filter: grayscale(0%) contrast(1.1);
  transform: scale(1.02);
}

.photo-meta {
  padding: 0.85rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.photo-name {
  font-family: var(--serif);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--white);
}

.photo-role {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  color: var(--pink);
  text-transform: uppercase;
}
</style>