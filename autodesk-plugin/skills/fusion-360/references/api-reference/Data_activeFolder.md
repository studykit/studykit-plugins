# Data.activeFolder Property

Parent Object: [Data](Data.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Data.h>

## Description

Gets the active DataFolder as seen in the Fusion Data Panel.

## Syntax

* [Python](#Python)
* [C++](#C++)

"data\_var" is a variable referencing a Data object. |

"data\_var" is a variable referencing a Data object. ```` ``` #include <Core/Dashboard/Data.h>  // Get the value of the property. Ptr<DataFolder> propertyValue = data_var->activeFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFolder](DataFolder.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |