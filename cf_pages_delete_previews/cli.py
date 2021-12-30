"""Console script for cf_pages_delete_previews."""
import argparse
import sys
import cf_pages_delete_previews

def main():
    """Console script for cf_pages_delete_previews."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--redact", action="store_true", default=False, required=False,
                        help="When \"--redact\" is used, project names will be replaced with IDs in log output.")
    argparser.add_argument("--whatif", action="store_true", default=False, required=False,
                        help="When \"--whatif\" is used, delete action will be deferred.")
    args = argparser.parse_args()
    
    projects = cf_pages_delete_previews.get_projects()
    for project in projects["result"]:
        cf_pages_delete_previews.delete_project_revisions(project, args)




if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
