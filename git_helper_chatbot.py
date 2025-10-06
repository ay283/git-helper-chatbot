import sys
import time


def type_print(text, delay=0.02):
    """Prints text with typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def type_input(prompt, delay=0.02):
    """Prints input prompt with typing effect, then waits for user input"""
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()


def handle_merge_conflict():
    type_print("\nLet's fix your merge conflict.")

    explain = type_input("Would you like me to explain what a merge conflict is? (yes/no): ").strip().lower()
    if explain in ["yes", "y"]:
        type_print("\nA merge conflict happens when Git can't automatically combine changes from different branches.")
    
    unmerged = type_input("\nRun `git status`. Do you see any files marked as 'unmerged'? (yes/no): ").strip().lower()
    if unmerged in ["no", "n"]:
        type_print("\nIf nothing is unmerged, your merge might already be resolved or aborted. Try `git merge --abort`.\n")
        return

    type_print("\nOpen one of the conflicted files. You'll see conflict markers like this:")
    type_print("<<<<<<< HEAD")
    type_print("your version of the code")
    type_print("=======")
    type_print("the incoming version from the other branch")
    type_print(">>>>>>> main")

    type_print("\nTo fix the conflict:")
    type_print("1. Decide which version you want to keep (or combine parts of both).")
    type_print("2. Delete the conflict markers (<<<<<<<, =======, >>>>>>>) after making your edits.")
    type_print("3. Save the file when you're done.")

    ready = type_input("\nHave you finished editing and removing the conflict markers? (yes/no): ").strip().lower()
    if ready in ["no", "n", "not yet"]:
        type_print("\nNo worries, take your time and run me again when you're ready.\n")
        return

    type_print("\nNow run:")
    type_print("git add <filename>")
    type_print("git commit")
    
    success = type_input("\nDid that work? (yes/no): ").strip().lower()
    if success in ["yes", "y"]:
        type_print("\nGreat job! You've resolved the merge conflict successfully.")
    else:
        type_print("\nTry `git merge --continue`. If issues persist, check `git status` again or restart with `git merge --abort`.")

    type_input("\nPress Enter to return to the main menu.\n")
    return


def handle_push_pull_errors():
    type_print("\nLet's troubleshoot your push/pull issue.")
    
    while True:
        action = type_input("Were you trying to push or pull? ").strip().lower()
        if "push" in action:
            type_print("\nIf your push was rejected because the remote has newer commits, try this:")
            type_print("1. Run: git pull --rebase origin main")
            type_print("2. Resolve any conflicts if prompted.")
            type_print("3. Run: git push origin main")
            
            follow_up = type_input("\nDid that work? (yes/no): ").strip().lower()
            if follow_up in ["no", "n"]:
                type_print("\nIf not, check that you're on the correct branch or have permission to push to this repo.")
            break
        elif "pull" in action:
            type_print("\nIf your pull failed, check your remote and branch names:")
            type_print("1. Run: git remote -v")
            type_print("2. Run: git branch -a")
            type_print("If there are conflicts, follow the merge conflict resolution steps.")
            break
        else: # Error Handling
            type_print("\nPush means sending changes to the remote repo; pull means bringing changes from it.")
            type_print("Please let me know which one you were doing.\n")

    type_input("\nPress Enter to return to the main menu.\n")
    return


def handle_undo_commit():
    type_print("\nLet's undo a commit.")
    while True:
        type_print("Do you want to:")
        type_print("1. Undo the last commit but keep changes staged")
        type_print("2. Undo the last commit and delete changes")
        type_print("3. Undo a specific commit")
        
        choice = type_input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            type_print("\nRun this command:")
            type_print("git reset --soft HEAD~1")
            type_print("This keeps your changes staged but removes the last commit.")
            break
        elif choice == "2":
            type_print("\nRun this command:")
            type_print("git reset --hard HEAD~1")
            type_print("This completely removes the last commit and its changes.")
            break
        elif choice == "3":
            type_print("\nRun this command:")
            type_print("git revert <commit-hash>")
            type_print("This creates a new commit that reverses the changes of a specific commit.")
            break
        else: # Error Handling
            type_print("\nThat's not a valid option. Please enter 1, 2, or 3.\n")

    type_print("After running your command, use `git log` to verify the result.")
    type_input("\nPress Enter to return to the main menu.\n")
    return


def handle_other():
    type_print("\nI'm sorry, I'm not able to help with other issues yet. You can check out the Git documentation at https://git-scm.com/docs.")
    type_input("\nPress Enter to return to the main menu.\n")
    return


def git_helper_chatbot():
    type_print("Hi, I'm Git Helper Bot.")

    while True:
        type_print("What can I help you with today?")
        type_print("1. Merge conflict\n2. Push/pull error\n3. Undoing a commit\n4. Something else\n5. Exit")
        
        choice = type_input("Enter your choice (1-5): ").strip().lower()
        if choice in ["1", "merge conflict"]:
            handle_merge_conflict()
        elif choice in ["2", "push/pull error"]:
            handle_push_pull_errors()
        elif choice in ["3", "undoing a commit"]:
            handle_undo_commit()
        elif choice in ["4", "something else"]:
            handle_other()
        elif choice in ["5", "exit", "quit"]:
            type_print("\nGlad I could help! Goodbye.")
            break
        else: # Error Handling
            type_print("\nThat's not an option. Please enter 1, 2, 3, 4, or 5.\n")


if __name__ == "__main__":
    git_helper_chatbot()
