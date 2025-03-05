/* script.js */

/**
 * Run any global initialization code when the DOM is fully loaded.
 */
document.addEventListener('DOMContentLoaded', () => {
    console.log('Site is loaded and DOM is ready!');
  
    // Example: if you want to apply some dynamic behavior to elements
    // (like toggling or showing/hiding certain components), you can do it here.
  
    // Let's say we have an element with ID 'globalAlert' we want to auto-hide after 3 seconds:
    const globalAlert = document.getElementById('globalAlert');
    if (globalAlert) {
      setTimeout(() => {
        globalAlert.style.display = 'none';
      }, 3000);
    }
  });
  
  /**
   * Example helper function to show an alert on the page.
   * Call this from your HTML or other scripts if needed.
   */
  function showAlert(message, type = 'info') {
    // Type can be: 'info', 'success', 'warning', 'danger', etc. for Bootstrap
    const alertPlaceholder = document.getElementById('alertPlaceholder');
    if (!alertPlaceholder) return;
  
    alertPlaceholder.innerHTML = `
      <div class="alert alert-${type}" role="alert">
        ${message}
      </div>
    `;
    
    // Auto-hide after 3 seconds (optional)
    setTimeout(() => {
      alertPlaceholder.innerHTML = '';
    }, 3000);
  }
  
  /**
   * (Optional) If you have repeated fetch logic across multiple pages
   * you could unify them here. 
   * For instance, a generic fetch helper that returns JSON.
   */
  async function fetchData(url) {
    try {
      const response = await fetch(url);
      return await response.json();
    } catch (err) {
      console.error('Error fetching:', err);
      throw err;
    }
  }
  