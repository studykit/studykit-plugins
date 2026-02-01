# Data.activeProject Property

Parent Object: [Data](Data.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Data.h>

## Description

Gets and sets the active DataProject. This is the project currently displayed in the Fusion Data Panel.

## Syntax

* [Python](#Python)
* [C++](#C++)

"data\_var" is a variable referencing a Data object. |

"data\_var" is a variable referencing a Data object. ```` ``` #include <Core/Dashboard/Data.h>  // Get the value of the property. Ptr<DataProject> propertyValue = data_var->activeProject();  // Set the value of the property, where value_var is a DataProject. bool returnValue = data_var->activeProject(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DataProject](DataProject.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |