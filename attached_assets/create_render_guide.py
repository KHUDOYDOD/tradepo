import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_signup_screenshot():
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create browser window style
    window = patches.Rectangle((0, 0), 10, 6, facecolor='white', edgecolor='gray')
    ax.add_patch(window)
    
    # Add Render.com header
    plt.text(0.5, 5.5, 'render.com', fontsize=14, weight='bold')
    
    # Add Sign Up button
    btn = patches.Rectangle((4, 3), 2, 0.5, facecolor='blue', alpha=0.3)
    ax.add_patch(btn)
    plt.text(4.3, 3.15, 'Sign Up with GitHub', color='black')
    
    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Save the figure
    plt.savefig('render_guide_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_new_service_screenshot():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Dashboard layout
    window = patches.Rectangle((0, 0), 10, 6, facecolor='white', edgecolor='gray')
    ax.add_patch(window)
    
    # Add New Service button
    btn = patches.Rectangle((1, 4), 2, 0.5, facecolor='green', alpha=0.3)
    ax.add_patch(btn)
    plt.text(1.3, 4.15, 'New +', color='black')
    
    # Add service options
    plt.text(1, 3, '• Web Service', fontsize=12)
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.savefig('render_guide_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_env_vars_screenshot():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Settings page layout
    window = patches.Rectangle((0, 0), 10, 6, facecolor='white', edgecolor='gray')
    ax.add_patch(window)
    
    # Environment Variables section
    plt.text(0.5, 5.5, 'Environment Variables', fontsize=14, weight='bold')
    
    # Add example variables
    plt.text(0.5, 4.5, 'BOT_TOKEN', fontsize=12)
    plt.text(0.5, 4, 'DATABASE_URL', fontsize=12)
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.savefig('render_guide_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_deploy_screenshot():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Deploy page layout
    window = patches.Rectangle((0, 0), 10, 6, facecolor='white', edgecolor='gray')
    ax.add_patch(window)
    
    # Add deploy settings
    plt.text(0.5, 5.5, 'Deploy Settings', fontsize=14, weight='bold')
    plt.text(0.5, 4.5, 'Build Command: pip install -r requirements.txt', fontsize=12)
    plt.text(0.5, 4, 'Start Command: python attached_assets/bot.py', fontsize=12)
    
    # Add deploy button
    btn = patches.Rectangle((4, 2), 2, 0.5, facecolor='blue', alpha=0.3)
    ax.add_patch(btn)
    plt.text(4.3, 2.15, 'Deploy', color='black')
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.savefig('render_guide_4.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_signup_screenshot()
    create_new_service_screenshot()
    create_env_vars_screenshot()
    create_deploy_screenshot()
