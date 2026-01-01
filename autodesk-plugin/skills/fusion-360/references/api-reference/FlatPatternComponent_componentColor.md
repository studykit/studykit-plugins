# FlatPatternComponent.componentColor Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Gets and sets the color associated with a component. This color is only used when the "Display Component Colors" command is enabled. Enabling the display of component colors is done through the command or API using the Application.isComponentColorsDisplayed property. When this is on, all bodies in a component will display using the color assigned to the component. Fusion randomly assigns a color to a component when it is created. This property allows you to get and change the assigned default color. Setting this property to null results in a new color being randomly assigned by Fusion. This is the equivalent of the "Cycle Component Color" command available in the context menu of a component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<Color> propertyValue = flatPatternComponent_var->componentColor();  // Set the value of the property, where value_var is a Color. bool returnValue = flatPatternComponent_var->componentColor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |