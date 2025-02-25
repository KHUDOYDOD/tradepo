import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_github_login_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Browser window
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # GitHub header
    plt.text(0.5, 0.9, 'github.com', fontsize=14, weight='bold', ha='center', transform=ax.transAxes)

    # Sign In form
    plt.text(0.5, 0.7, 'Ба GitHub ворид шавед', fontsize=12, ha='center', transform=ax.transAxes)

    # Sign In button
    btn = patches.Rectangle((0.4, 0.4), 0.2, 0.1, facecolor='green', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.5, 0.45, 'Воридшавӣ', color='black', ha='center', transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('github_guide_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_new_repo_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Browser window
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # GitHub header with + button
    plt.text(0.2, 0.9, 'github.com', fontsize=14, weight='bold', transform=ax.transAxes)
    btn = patches.Rectangle((0.7, 0.85), 0.1, 0.1, facecolor='gray', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.75, 0.9, '+', color='black', ha='center', transform=ax.transAxes)

    # New repository option
    plt.text(0.75, 0.8, 'Репозиторияи нав', fontsize=10, ha='center', transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('github_guide_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_repo_setup_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Browser window
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # Repository setup form
    plt.text(0.5, 0.9, 'Эҷоди репозиторияи нав', fontsize=14, weight='bold', ha='center', transform=ax.transAxes)
    plt.text(0.2, 0.7, 'Номи репозитория: forex-analysis-bot', fontsize=12, transform=ax.transAxes)

    # Create repository button
    btn = patches.Rectangle((0.4, 0.3), 0.2, 0.1, facecolor='green', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.5, 0.35, 'Эҷод кардан', color='black', ha='center', transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('github_guide_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_upload_files_screenshot():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)

    # Browser window
    window = patches.Rectangle((0.1, 0.1), 0.8, 0.8, facecolor='white', edgecolor='gray', transform=ax.transAxes)
    ax.add_patch(window)

    # Upload interface
    plt.text(0.5, 0.9, 'Боргузории файлҳо', fontsize=14, weight='bold', ha='center', transform=ax.transAxes)
    plt.text(0.5, 0.7, 'Файлҳоро ба ин ҷо кашед\nё барои интихоб пахш кунед', fontsize=12, ha='center', transform=ax.transAxes)

    # Commit changes button
    btn = patches.Rectangle((0.4, 0.3), 0.2, 0.1, facecolor='green', alpha=0.3, transform=ax.transAxes)
    ax.add_patch(btn)
    plt.text(0.5, 0.35, 'Сабт кардан', color='black', ha='center', transform=ax.transAxes)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.savefig('github_guide_4.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_github_login_screenshot()
    create_new_repo_screenshot()
    create_repo_setup_screenshot()
    create_upload_files_screenshot()