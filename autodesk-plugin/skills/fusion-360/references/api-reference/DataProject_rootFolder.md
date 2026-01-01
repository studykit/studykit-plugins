# DataProject.rootFolder Property

Parent Object: [DataProject](DataProject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProject.h>

## Description

Returns the project's root folder. This provides access to all of the folders and the files in the top level of the project.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProject\_var" is a variable referencing a DataProject object. |

"dataProject\_var" is a variable referencing a DataProject object. ```` ``` #include <Core/Dashboard/DataProject.h>  // Get the value of the property. Ptr<DataFolder> propertyValue = dataProject_var->rootFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFolder](DataFolder.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |