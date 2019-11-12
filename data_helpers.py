import pandas as pd
import re


def explode_protocol_summary(text):
    items = re.findall("<b>(.*?)</b>", text)
    values = re.findall("</b>(.*?)<b>", text)
    protocol = "standard"
    body_part = oral_contrast = iv_contrast = ""
    try:
        if len(values) != len(items):
            values.append(re.findall("(?s:.*)</b>(.*?)$", text)[-1].split("|")[0])
    except:
        pass
    processed_values = []
    for s in values:
        processed_values.append(",".join(string for string in s.split("|") if len(string) > 0))
    if len(items) == 3:
        items.insert(0, "Protocol:")
        processed_values.insert(0, "Standard")
    for i in range(len(items)):
        if items[i] == "Protocol:":
            protocol = processed_values[i]
        if items[i] == "Body Part:":
            body_part = processed_values[i]
        if items[i] == "Oral Contrast:":
            oral_contrast = processed_values[i]
        if items[i] == "IV Contrast:":
            iv_contrast = processed_values[i]
    return (protocol, body_part, oral_contrast, iv_contrast)