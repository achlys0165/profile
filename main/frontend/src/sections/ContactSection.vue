<template>
  <section id="contact" class="wrap">
    <div class="ed-header rv" v-reveal>
      <div class="ed-num">06</div>
      <div class="ed-title-block">
        <p class="ed-label">Reach Out</p>
        <h2 class="ed-title">Let's <em>Connect</em></h2>
      </div>
    </div>
    
    <div class="contact-layout rv rv-d1" v-reveal>
      <div class="contact-info">
        <p class="contact-quote">"I'm always looking to learn from people who know more than I do."</p>
        <p class="contact-p">Whether you want to talk security, collaborate on a project, or just exchange notes — I'm open to it.</p>
        
        <div class="clinks">
          <ContactLink v-for="link in links" :key="link.label" :link="link" />
        </div>
        
        <div class="status-indicator">
          <span class="status-dot" :class="{ online: apiStatus }"></span>
          <span class="status-text">{{ apiStatus ? 'API Online' : 'API Offline' }}</span>
        </div>
      </div>
      
      <form class="cf" @submit.prevent="sendMessage">
        <div class="cf-row">
          <div class="fl">
            <label>Name *</label>
            <input 
              v-model="form.name" 
              type="text" 
              class="cfi" 
              placeholder="your name" 
              required
              :disabled="isSending"
            >
          </div>
          <div class="fl">
            <label>Email *</label>
            <input 
              v-model="form.email" 
              type="email" 
              class="cfi" 
              placeholder="you@example.com" 
              required
              :disabled="isSending"
            >
          </div>
        </div>
        
        <div class="fl">
          <label>Message</label>
          <textarea 
            v-model="form.message" 
            class="cft" 
            placeholder="What's on your mind?"
            :disabled="isSending"
          ></textarea>
        </div>
        
        <div class="form-footer">
          <button 
            type="submit" 
            class="btn btn-pri" 
            :disabled="isSending || !form.name || !form.email"
          >
            <span v-if="isSending" class="spinner"></span>
            {{ isSending ? 'Sending...' : (sent ? 'Sent ✓' : 'Send Message →') }}
          </button>
          
          <span v-if="error" class="error-msg">{{ error }}</span>
          <span v-if="sent && !error" class="success-msg">Message sent! I'll get back to you soon.</span>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ContactLink from './ContactLink.vue'
import { api } from '../services/api.js'
import { vReveal } from '../directives/reveal'

const links = [
  { icon: '✉', label: 'jansultan905@gmail.com', href: 'jansultan905@gmail.com' },
  { icon: '⌥', label: 'github.com/achlys0165', href: 'http://github.com/achlys0165', ext: true },
  { icon: '◈', label: 'linkedin.com/in/jansultan0210', href: 'http://www.linkedin.com/in/jansultan0210', ext: true },
  { icon: '🎯', label: 'TryHackMe Profile', href: 'https://tryhackme.com/p/jgsultan', ext: true }
]

const form = ref({ name: '', email: '', message: '' })
const isSending = ref(false)
const sent = ref(false)
const error = ref('')
const apiStatus = ref(false)

const checkStatus = async () => {
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/health`)
    apiStatus.value = res.ok
  } catch (e) {
    apiStatus.value = false
  }
}

const sendMessage = async () => {
  if (!form.value.name || !form.value.email) return
  
  isSending.value = true
  error.value = ''
  
  try {
    const res = await api.sendContact({
      name: form.value.name,
      email: form.value.email,
      message: form.value.message
    })
    
    if (res.success) {
      form.value = { name: '', email: '', message: '' }
      sent.value = true
      setTimeout(() => sent.value = false, 5000)
    }
  } catch (e) {
    error.value = 'Failed to send. Please try again or email directly.'
    console.error(e)
  } finally {
    isSending.value = false
  }
}

onMounted(() => {
  checkStatus()
  setInterval(checkStatus, 30000)
})
</script>

<style scoped>
.contact-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: start;
}

.contact-info {
  display: flex;
  flex-direction: column;
}

.contact-quote {
  font-family: var(--serif);
  font-style: italic;
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
  color: var(--pink-pale);
  line-height: 1.5;
  margin-bottom: 2.5rem;
  border-left: 2px solid var(--pink);
  padding-left: 1.5rem;
}

.contact-p {
  font-size: 14px;
  color: var(--muted2);
  font-weight: 300;
  line-height: 1.75;
  margin-bottom: 2rem;
}

.clinks {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--mono);
  font-size: 11px;
  color: var(--muted2);
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--muted2);
  transition: background 0.3s;
}

.status-dot.online {
  background: #28c840;
  box-shadow: 0 0 8px #28c840;
}

.cf {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
}

.cf-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.9rem;
}

.form-footer {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.spinner {
  display: inline-block;
  width: 12px;
  height: 12px;
  border: 2px solid var(--ink);
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: 6px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-msg {
  color: #ff6b6b;
  font-size: 12px;
  font-family: var(--mono);
}

.success-msg {
  color: var(--pink);
  font-size: 12px;
  font-family: var(--mono);
}

@media (max-width: 860px) {
  .contact-layout {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  
  .cf-row {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 861px) and (max-width: 1024px) {
  .contact-layout {
    gap: 3rem;
  }
}
</style>