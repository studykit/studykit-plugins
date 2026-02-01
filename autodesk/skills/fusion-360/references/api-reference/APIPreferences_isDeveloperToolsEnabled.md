# APIPreferences.isDeveloperToolsEnabled Property

Parent Object: [APIPreferences](APIPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

Gets and sets if access to "Developer Tools" should be enabled in pallets and BrowserCommandInputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"aPIPreferences\_var" is a variable referencing an APIPreferences object. |

"aPIPreferences\_var" is a variable referencing an APIPreferences object. ```` ``` #include <Core/Application/APIPreferences.h>  // Get the value of the property. boolean propertyValue = aPIPreferences_var->isDeveloperToolsEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = aPIPreferences_var->isDeveloperToolsEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |