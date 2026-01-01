# PrintSettingQuery.execute Method

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

Query for specific PrintSettings. This PrintSettingQuery query.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a [PrintSettingQuery](PrintSettingQuery.htm) object.```` ``` returnValue = printSettingQuery_var.execute() ``` ```` |

"printSettingQuery\_var" is a variable referencing a [PrintSettingQuery](PrintSettingQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PrintSetting](PrintSetting.htm)[] | Returns a list of PrintSetting. Each returned PrintSetting matches this query. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |