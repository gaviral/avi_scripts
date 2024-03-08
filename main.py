#!/usr/bin/env python3

import subprocess


def update_homebrew():
    print("\n\nUpdating Homebrew...")
    subprocess.run(["brew", "update"])


def upgrade_homebrew_packages():
    print("\n\nUpgrading Homebrew packages...")
    subprocess.run(["brew", "upgrade"])


def upgrade_pyenv():
    print("\n\nUpgrading pyenv...")
    subprocess.run(["brew", "upgrade", "pyenv"])


def run_all_updates():
    update_homebrew()
    upgrade_homebrew_packages()
    upgrade_pyenv()


def main():
    actions = {"1": update_homebrew, "2": upgrade_homebrew_packages, "3": upgrade_pyenv, "4": run_all_updates, }
    while True:
        print("\n\nSelect an option:")
        print("1) Update Homebrew")
        print("2) Upgrade Homebrew packages")
        print("3) Update pyenv")
        print("4) Run all updates in sequence")
        print("5) Exit")
        option = input("Enter option: ").strip()

        if option == "5":
            print("Exiting...")
            break
        elif option in actions:
            actions[option]()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
