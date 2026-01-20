def validate_fix(file, change):
    forbidden = ["terraform destroy", "rm -rf", "DROP TABLE"]

    for word in forbidden:
        if word in change:
            return False

    return True
