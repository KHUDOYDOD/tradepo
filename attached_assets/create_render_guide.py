import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_signup_screenshot():
    # Create figure and axis with larger dimensions
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Create browser window style
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # Add Render.com header
    plt.text(0.5, 0.9, 'render.com', fontsize=14, weight='bold', ha='center', transform=ax.transAxes)

    # Add Sign Up button
    btn = patches.Rectangle((0.4, 0.5), 0.2, 0.1, facecolor='blue', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.5, 0.55, 'Sign Up with GitHub', color='black', ha='center', transform=ax.transAxes)

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Save with higher quality
    plt.savefig('render_guide_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_new_service_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Dashboard layout
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # Add New Service button
    btn = patches.Rectangle((0.2, 0.7), 0.2, 0.1, facecolor='green', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.3, 0.75, 'New +', color='black', ha='center', transform=ax.transAxes)

    # Add service options
    plt.text(0.2, 0.5, '• Web Service', fontsize=12, transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('render_guide_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_env_vars_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Settings page layout
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # Environment Variables section
    plt.text(0.2, 0.9, 'Environment Variables', fontsize=14, weight='bold', transform=ax.transAxes)

    # Add example variables
    plt.text(0.2, 0.7, 'BOT_TOKEN', fontsize=12, transform=ax.transAxes)
    plt.text(0.2, 0.6, 'DATABASE_URL', fontsize=12, transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('render_guide_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_deploy_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Deploy page layout
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # Add deploy settings
    plt.text(0.2, 0.9, 'Deploy Settings', fontsize=14, weight='bold', transform=ax.transAxes)
    plt.text(0.2, 0.7, 'Build Command: pip install -r requirements.txt', fontsize=12, transform=ax.transAxes)
    plt.text(0.2, 0.6, 'Start Command: python attached_assets/bot.py', fontsize=12, transform=ax.transAxes)

    # Add deploy button
    btn = patches.Rectangle((0.4, 0.3), 0.2, 0.1, facecolor='blue', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.5, 0.35, 'Deploy', color='black', ha='center', transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('render_guide_4.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_signup_screenshot()
    create_new_service_screenshot()
    create_env_vars_screenshot()
    create_deploy_screenshot()