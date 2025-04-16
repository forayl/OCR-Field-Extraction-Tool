from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="PP-StructureV3")

output = pipeline.predict(
    input="./example.png",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    use_table_recognition=True,
)
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_json(save_path="output") ## 保存当前图像的结构化json结果
    res.save_to_markdown(save_path="output") ## 保存当前图像的markdown格式的结果
    res.save_to_img(save_path="output") ## 保存当前图像的预测结果
