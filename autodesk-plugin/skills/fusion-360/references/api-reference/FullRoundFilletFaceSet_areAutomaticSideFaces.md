# FullRoundFilletFaceSet.areAutomaticSideFaces Property

Parent Object: [FullRoundFilletFaceSet](FullRoundFilletFaceSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FullRoundFilletFaceSet.h>

## Description

Property that returns a boolean value indicating whether the side faces are used as automatically inferred side faces. It returns true indicating that the side faces are not being shown in the dialog when the user edits the feature. Calling the setSideFaces method will cause this property to be changed to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fullRoundFilletFaceSet\_var" is a variable referencing a FullRoundFilletFaceSet object. |

"fullRoundFilletFaceSet\_var" is a variable referencing a FullRoundFilletFaceSet object. ```` ``` #include <Fusion/Features/FullRoundFilletFaceSet.h>  // Get the value of the property. boolean propertyValue = fullRoundFilletFaceSet_var->areAutomaticSideFaces(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |