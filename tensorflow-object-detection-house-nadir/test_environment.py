import sys

def main():

    # get the system major version, which must be at least three
    system_major = sys.version_info.major

    if system_major != required_major:
        raise TypeError(
            "This project requires Python 3. Found: Python {}".format(sys.version)
        )

    # see if arcpy is installed on the system
    try:
        import arcpy
    except:
        raise TypeError(
            "This project requires the ArcPy module installed with ArcGIS."
        )
    
    print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
