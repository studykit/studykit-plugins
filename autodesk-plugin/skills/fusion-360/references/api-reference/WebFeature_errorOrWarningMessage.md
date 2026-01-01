# WebFeature.errorOrWarningMessage Property

Parent Object: [WebFeature](WebFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeature.h>

## Description

Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeature\_var" is a variable referencing a WebFeature object. |

"webFeature\_var" is a variable referencing a WebFeature object. ```` ``` #include <Fusion/Features/WebFeature.h>  // Get the value of the property. string propertyValue = webFeature_var->errorOrWarningMessage(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |