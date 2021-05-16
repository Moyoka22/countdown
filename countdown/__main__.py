from .main import main, parse_script_arguments

if __name__ == '__main__':
    args = parse_script_arguments()
    main(vars(args))
