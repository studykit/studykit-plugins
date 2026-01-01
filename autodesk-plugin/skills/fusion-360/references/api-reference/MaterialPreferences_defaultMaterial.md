# MaterialPreferences.defaultMaterial Property

Parent Object: [MaterialPreferences](MaterialPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MaterialPreferences.h>

## Description

Gets and sets the default material.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialPreferences\_var" is a variable referencing a MaterialPreferences object. |

"materialPreferences\_var" is a variable referencing a MaterialPreferences object. ```` ``` #include <Core/Application/MaterialPreferences.h>  // Get the value of the property. Ptr<Material> propertyValue = materialPreferences_var->defaultMaterial();  // Set the value of the property, where value_var is a Material. bool returnValue = materialPreferences_var->defaultMaterial(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Material](Material.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |