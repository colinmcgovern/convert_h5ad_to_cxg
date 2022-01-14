from os import path
from server.converters.h5ad_data_file import H5ADDataFile

def convert_to_cxg(
    input_file,
    output_directory,
    backed,
    title,
    about,
    sparse_threshold,
    obs_names,
    var_names,
    disable_custom_colors,
    disable_corpora_schema,
    overwrite,
):
    """
    Convert a dataset file into CXG.
    """

    print("step 1")

    h5ad_data_file = H5ADDataFile(
        input_file, backed, title, about, obs_names, var_names, use_corpora_schema=not disable_corpora_schema
    )

    print("step 2")

    # Get the directory that will hold all the CXG files
    cxg_output_container = get_output_directory(input_file, output_directory, overwrite)

    print("step 3")

    h5ad_data_file.to_cxg(
        cxg_output_container, sparse_threshold, convert_anndata_colors_to_cxg_colors=not disable_custom_colors
    )

    print("Done")

def get_output_directory(input_filename, output_directory, should_overwrite):
    """
    Get the name of the CXG output directory to be created/populated during the dataset conversion.
    """

    if output_directory and (not path.isdir(output_directory) or (path.isdir(output_directory) and should_overwrite)):
        if output_directory.endswith(".cxg"):
            return output_directory
        return output_directory + ".cxg"
    if output_directory and path.isdir(output_directory) and not should_overwrite:
        raise click.BadParameter(
            # f"Output directory {output_directory} already exists. If you'd like to overwrite, then run the command "
            # f"with the --overwrite flag."
        )

    return path.splitext(input_filename)[0] + ".cxg"

convert_to_cxg(
    '/home/colin/Desktop/h5ad/t1d.h5ad',
    '/home/colin/Desktop/test/t1d.cxg',
    False,
    "test",
    "test2",
    0.0,
    "",
    "",
    False,
    True,
    True)
