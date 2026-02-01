# Setup.printSetting Property

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Gets and sets the PrintSetting associated with the setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a Setup object. |

"setup\_var" is a variable referencing a Setup object. ```` ``` #include <Cam/CAM/Setup.h>  // Get the value of the property. Ptr<PrintSetting> propertyValue = setup_var->printSetting();  // Set the value of the property, where value_var is a PrintSetting. bool returnValue = setup_var->printSetting(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PrintSetting](PrintSetting.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |