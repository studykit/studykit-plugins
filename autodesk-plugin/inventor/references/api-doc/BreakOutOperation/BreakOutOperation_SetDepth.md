# BreakOutOperation.SetDepth Method

Parent Object: [BreakOutOperation](../BreakOutOperation/BreakOutOperation.md)

## Description

Method that sets the depth of the break out.

## Syntax

BreakOutOperation.**SetDepth**( [***DepthSource***] As Variant, [***DepthValue***] As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DepthSource | Variant | Graphic object that defines the depth of the break out. This argument is optional in the case where the depth is defined by a point (DepthType property returns kFromPointBreakOutType) and you only want to modify the depth value.  Several different types of objects can be used as input depending on how the depth of the break is to be defined. Here are the various valid inputs. 1. A **GeometryIntent** object that represents a point. This specifies the starting point of the break out area. In this case, the DepthValue argument must be specified to indicate the depth of the break out area from the specified point. 2. A **DrawingSketch** object which is associated with a dependant projected view. 3. A **DrawingCurve** object that is used to specify a 'hole'. A hole in this case is any geometry from a HoleFeature object or any cylinder or cone in the model. The axis of the hole, cylinder, or cone must be parallel to the sheet plane. The axis defines the depth of the hole. 4. A **PartComponentDefinition** object to indicate that the entire part is to be cut. This is only applicable when the drawing view contains a part. The PartComponentDefinition supplied must be the component definition of the part in the view. 5. A **ComponentOccurrence** (or a ComponentOccurrenceProxy) object in the context of the parent drawing view. The depth is defined by the depth of the associated part. This is only applicable when the drawing view contains an assembly. 6. An **ObjectCollection** containing multiple ComponentOccurrence (or ComponentOccurrenceProxy) objects. The depth is defined by the depths of the associated parts. This is only applicable when the drawing view contains an assembly. |
| DepthValue | Double | This argument is only applicable when the DepthType is already kFromPointBreakOutType or you're setting the depth type to be measured from a point. If it is already kFromPointBreakOutType and you want to use the existing from point you can just provide a new depth value. If you want set or change the depth point then the DepthSource argument must also be used to define the new from point. In all other cases the value of this argument is ignored. The value is always input as centimeters.   This is an optional argument whose default value is 0.0. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |