# Component.componentColor Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets the color associated with a component. This color is only used when the "Display Component Colors" command is enabled. Enabling the display of component colors is done through the command or API using the Application.isComponentColorsDisplayed property. When this is on, all bodies in a component will display using the color assigned to the component. Fusion randomly assigns a color to a component when it is created. This property allows you to get and change the assigned default color. Setting this property to null results in a new color being randomly assigned by Fusion. This is the equivalent of the "Cycle Component Color" command available in the context menu of a component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<Color> propertyValue = component_var->componentColor();  // Set the value of the property, where value_var is a Color. bool returnValue = component_var->componentColor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |