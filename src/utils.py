import re

pat_doc_type = re.compile(
    r"""
    (?:采购)?(?:项目)?
    (
        [（的-]?
        (?:重新)?
        (?:
            (?:
                (?:成交|中标|结果|暂停|废标|终止|延期|更正|变更|更改|竞争性|谈判|磋商|询价|单一来源|终止|邀请|补充|暂缓|澄清|失败|资格预审)+
                (?:信息|事项)?
                (?:公告|书|公示|通知)?
            )|
            (?:(?:公开)?招标)?
            公告
        )
        ）?
    )
    """
)

pat_projet_id = re.compile(
    r"（项目编号(?:（.*?）)?(?::|：)?\s*\S+[a-zA-Z0-9号#]）"
)

pat_other_id = re.compile(
            r"（(?:采购计划|招标(?:文件)?)编号(?:（.*?）)?(?::|：)?\s*\S+[a-zA-Z0-9号#]）"
        )

pat_only_id = re.compile(
    r"（[a-zA-Z\d-]+）"
)

def net_object(text):
    # remove document type
    text = pat_doc_type.sub("", text)
    # remove project/notice document id
    text = pat_projet_id.sub("", text)
    text = pat_other_id.sub("", text)
    text = pat_only_id.sub("", text)
    # remove agency
    text = text.split("关于", maxsplit=1)[-1]
    # remove special chars and project ids
    text = re.sub("\W", "", text)
    text = re.sub("[a-zA-Z\d]", "", text)
    return text

def net_trade(text):
    if text:
        trades = text.split(",")
        trades_short = list(set([trade.split("/")[0] for trade in trades]).intersection({"工程", "货物", "服务"}))
        # in case of multiple trade: keep first one
        return trades_short[0]
    else:
        return ""