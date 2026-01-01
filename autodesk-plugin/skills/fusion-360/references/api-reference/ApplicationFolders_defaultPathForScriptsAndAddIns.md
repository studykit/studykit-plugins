# ApplicationFolders.defaultPathForScriptsAndAddIns Property

Parent Object: [ApplicationFolders](ApplicationFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationFolders.h>

## Description

Gets and sets the default path for scripts and add-ins. This is the same as the defaultPathForScriptsAndAddIns property on the APIPreferences object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. |

"applicationFolders\_var" is a variable referencing an ApplicationFolders object. ```` ``` #include <Core/Application/ApplicationFolders.h>  // Get the value of the property. string propertyValue = applicationFolders_var->defaultPathForScriptsAndAddIns();  // Set the value of the property, where value_var is a string. bool returnValue = applicationFolders_var->defaultPathForScriptsAndAddIns(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |