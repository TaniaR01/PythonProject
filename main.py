from Upload import uploader
uploader_obj = uploader()
uploader_obj.load_df("netflix.csv")
uploader_obj.preview_10_df()