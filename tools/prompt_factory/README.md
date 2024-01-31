# 文件说明

 - prompt_maker.json  负责 prompt 生成和基础信息语料抽取的 json 配置
 - web_demo.py  供通用型的 prompt 产出调试，可以不断修改 `src/prompt` 中的 `prompt.json`来调试通用型的 prompt。目前只支持 gpt 。
 - prompt_to_json_in_bulk.py 负责批量将test/prompt下的.md prompt文件，转化为 tianji/prompt 下的json格式
 - check_prompt_template_in_bulk.py 用于批量检查test/prompt下的.md prompt文件是否符合 test/08-None-prompt编写规则模板.md中的格式



# demo 运行

首先安装依赖

```shell
pip install streamlit
pip install openai==0.28.0
pip install python-dotenv
```

在项目根目录下的`.env`文件中可以修改你使用的openai_key，形式为OPENAI_API_KEY="sk-..."

使用以下命令运行web_demo

```shell
streamlit run tools/prompt_factory/web_demo.py
```

prompt 需要在 `tianji\prompt\gpt_prompt\prompt.json` 文件中修改。
现在只是在 `prompt.json` 中添加了一个全局指令和一个根据用户描述的场景得到的user_prompt，可以在 `web_demo` 中看到效果。大家可以在 `prompt.json` 中添加自己任务的prompt，然后在 `web_demo` 中修改加载项。 

prompt_to_json_in_bulk.py 填写文件夹即可使用
prompt_to_json_for_CI.py 需要填写文件路径(为之后的CI准备)

**当前效果**
本demo能够根据用户输入（描述需要使用social-ai的敬酒场景）返回对话语言

prompt_to_json_in_bulk.py
运行完后会在tianji/prompt文件夹下获得对应的json文档

