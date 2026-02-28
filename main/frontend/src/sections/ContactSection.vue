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
      </div>
      
      <!-- Formspree Contact Form -->
      <form 
        :action="formspreeUrl" 
        method="POST"
        class="cf"
        @submit.prevent="handleSubmit"
      >
        <!-- Hidden field for redirect after submission -->
        <input type="hidden" name="_next" :value="redirectUrl">
        
        <!-- Optional: subject line -->
        <input type="hidden" name="_subject" value="New message from portfolio">
        
        <!-- Optional: disable captcha -->
        <input type="hidden" name="_captcha" value="false">
        
        <div class="cf-row">
          <div class="fl">
            <label for="name">Name *</label>
            <input 
              id="name"
              v-model="form.name"
              type="text" 
              name="name"
              class="cfi" 
              placeholder="your name" 
              required
              :disabled="isSubmitting"
            >
          </div>
          <div class="fl">
            <label for="email">Email *</label>
            <input 
              id="email"
              v-model="form.email"
              type="email" 
              name="email"
              class="cfi" 
              placeholder="you@example.com" 
              required
              :disabled="isSubmitting"
            >
          </div>
        </div>
        
        <div class="fl">
          <label for="message">Message *</label>
          <textarea 
            id="message"
            v-model="form.message"
            name="message"
            class="cft" 
            placeholder="What's on your mind?"
            required
            :disabled="isSubmitting"
          ></textarea>
        </div>
        
        <div class="form-footer">
          <button 
            type="submit" 
            class="btn btn-pri" 
            :disabled="isSubmitting || !form.name || !form.email || !form.message"
          >
            <span v-if="isSubmitting" class="spinner"></span>
            {{ buttonText }}
          </button>
          
          <span v-if="status === 'success'" class="success-msg">
            Message sent! I'll get back to you soon.
          </span>
          <span v-if="status === 'error'" class="error-msg">
            Something went wrong. Please try again.
          </span>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import ContactLink from './ContactLink.vue'
import { vReveal } from '../directives/reveal'

const formspreeId = 'mnjbrlqa' // e.g., 'xeqwdyky'
const formspreeUrl = `https://formspree.io/f/${formspreeId}`
const redirectUrl = 'https://jan-sultan.vercel.app?message=sent'

const links = [
  { icon: '✉', label: 'jansultan905@gmail.com', href: 'jansultan905@gmail.com' },
  { icon: '⌥', label: 'github.com/achlys0165', href: 'http://github.com/achlys0165', ext: true },
  { icon: '◈', label: 'linkedin.com/in/jansultan0210', href: 'http://www.linkedin.com/in/jansultan0210', ext: true },
  { icon: '🎯', label: 'TryHackMe Profile', href: 'https://tryhackme.com/p/jgsultan', ext: true }
]

const form = ref({ name: '', email: '', message: '' })
const isSubmitting = ref(false)
const status = ref('idle') // 'idle' | 'submitting' | 'success' | 'error'

const buttonText = computed(() => {
  if (isSubmitting.value) return 'Sending...'
  if (status.value === 'success') return 'Sent ✓'
  return 'Send Message →'
})

const handleSubmit = async (e) => {
  isSubmitting.value = true
  status.value = 'submitting'
  
  try {
    const response = await fetch(formspreeUrl, {
      method: 'POST',
      body: new FormData(e.target),
      headers: {
        'Accept': 'application/json'
      }
    })
    
    if (response.ok) {
      status.value = 'success'
      form.value = { name: '', email: '', message: '' }
    } else {
      status.value = 'error'
    }
  } catch (err) {
    console.error('Form submission error:', err)
    status.value = 'error'
  } finally {
    isSubmitting.value = false
  }
}
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
  margin-top: 0.5rem;
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

.success-msg {
  color: var(--pink);
  font-size: 12px;
  font-family: var(--mono);
}

.error-msg {
  color: #ff6b6b;
  font-size: 12px;
  font-family: var(--mono);
}

/* Disable default form styles */
.cf:disabled {
  opacity: 0.7;
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
</style>
