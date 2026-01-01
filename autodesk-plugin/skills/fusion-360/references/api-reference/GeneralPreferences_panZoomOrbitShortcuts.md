# GeneralPreferences.panZoomOrbitShortcuts Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets how pan, zoom, and orbit should behave.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. PanZoomOrbitShortcuts propertyValue = generalPreferences_var->panZoomOrbitShortcuts();  // Set the value of the property, where value_var is a PanZoomOrbitShortcuts. bool returnValue = generalPreferences_var->panZoomOrbitShortcuts(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PanZoomOrbitShortcuts](PanZoomOrbitShortcuts.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |