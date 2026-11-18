import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import HelloOrigame from '../HelloOrigame.vue'

describe('HelloOrigame', () => {
  it('affiche le prénom reçu en prop', () => {
    const wrapper = mount(HelloOrigame, { props: { name: 'Rodrigue' } })
    expect(wrapper.text()).toContain('Bonjour Rodrigue')
  })
})
