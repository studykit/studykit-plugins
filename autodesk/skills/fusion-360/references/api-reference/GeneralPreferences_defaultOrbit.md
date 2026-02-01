# GeneralPreferences.defaultOrbit Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Get and sets the type of orbit.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. DefaultOrbits propertyValue = generalPreferences_var->defaultOrbit();  // Set the value of the property, where value_var is a DefaultOrbits. bool returnValue = generalPreferences_var->defaultOrbit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DefaultOrbits](DefaultOrbits.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |