# PrintSettingQuery.url Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

The URL specifies the location and folder to search for in the PrintSetting library. Setting the URL updates the location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. Ptr<URL> propertyValue = printSettingQuery_var->url();  // Set the value of the property, where value_var is a URL. bool returnValue = printSettingQuery_var->url(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |