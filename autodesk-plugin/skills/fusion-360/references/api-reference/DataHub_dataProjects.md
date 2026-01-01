# DataHub.dataProjects Property

Parent Object: [DataHub](DataHub.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

Returns the projects within this hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHub\_var" is a variable referencing a DataHub object. |

"dataHub\_var" is a variable referencing a DataHub object. ```` ``` #include <Core/Dashboard/DataHub.h>  // Get the value of the property. Ptr<DataProjects> propertyValue = dataHub_var->dataProjects(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataProjects](DataProjects.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |