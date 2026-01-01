# GeneralPreferences.defaultModelingOrientation Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets the default for which direction is considered "up".

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. DefaultModelingOrientations propertyValue = generalPreferences_var->defaultModelingOrientation();  // Set the value of the property, where value_var is a DefaultModelingOrientations. bool returnValue = generalPreferences_var->defaultModelingOrientation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DefaultModelingOrientations](DefaultModelingOrientations.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |