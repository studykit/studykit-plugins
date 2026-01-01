# APIPreferences.defaultPathForScriptsAndAddIns Property

Parent Object: [APIPreferences](APIPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

The default path where new scripts or add-ins will be created. Scripts will be created in a "Scripts" subdirectory and add-ins will be created in an "AddIns" subdirectory. This must be the full path to the parent folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"aPIPreferences\_var" is a variable referencing an APIPreferences object.  ```` ``` # Get the value of the property. propertyValue = aPIPreferences_var.defaultPathForScriptsAndAddIns  # Set the value of the property. aPIPreferences_var.defaultPathForScriptsAndAddIns = propertyValue ``` ```` |

"aPIPreferences\_var" is a variable referencing an APIPreferences object. ```` ``` #include <Core/Application/APIPreferences.h>  // Get the value of the property. string propertyValue = aPIPreferences_var->defaultPathForScriptsAndAddIns();  // Set the value of the property, where value_var is a string. bool returnValue = aPIPreferences_var->defaultPathForScriptsAndAddIns(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |