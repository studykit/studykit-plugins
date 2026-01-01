# ShellFeature.outsideThickness Property

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

Gets the outside thickness. Edit the thickness through ModelParameter. This property returns nothing in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a ShellFeature object. |

"shellFeature\_var" is a variable referencing a ShellFeature object. ```` ``` #include <Fusion/Features/ShellFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = shellFeature_var->outsideThickness(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |