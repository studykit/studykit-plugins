# PrintSettingQuery.location Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

The location specifies the location to search in the PrintSetting library. Setting the location clears any previous specified URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. LibraryLocations propertyValue = printSettingQuery_var->location();  // Set the value of the property, where value_var is a LibraryLocations. bool returnValue = printSettingQuery_var->location(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LibraryLocations](LibraryLocations.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |