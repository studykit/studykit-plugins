# Sketch.baseOrFormFeature Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

This property returns the base or form feature that this sketch is associated with. It returns null in the case where the sketch is parametrically defined and is not related to a base or form feature. It also returns null in a direct modeling design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<Base> propertyValue = sketch_var->baseOrFormFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |