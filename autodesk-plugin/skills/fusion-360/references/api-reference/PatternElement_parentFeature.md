# PatternElement.parentFeature Property

Parent Object: [PatternElement](PatternElement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

Gets the feature pattern this element is a member of.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElement\_var" is a variable referencing a PatternElement object. |

"patternElement\_var" is a variable referencing a PatternElement object. ```` ``` #include <Fusion/Features/PatternElement.h>  // Get the value of the property. Ptr<Feature> propertyValue = patternElement_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |