# BreakOutOperations.Add Method

Parent Object: [BreakOutOperations](../BreakOutOperations/BreakOutOperations.md)

## Description

Method that adds a break out to a drawing view. The newly created BreakOutOperation object is returned.

## Syntax

BreakOutOperations.**Add**( ***Profile*** As [Profile](../Profile/Profile.md), ***DepthSource*** As Object, [***DepthValue***] As Double, [***SectionAllParts***] As Boolean ) As [BreakOutOperation](../BreakOutOperation/BreakOutOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object that specifies the sketch profile for the break out. This profile must be closed so it should be created using the AddForSolid method of the Profiles object. |
| DepthSource | Object | Input object that specifies the source for the break out depth. Valid input objects are:  1. A **GeometryIntent** object that represents a point. This specifies the starting point of the break out area. In this case, the DepthValue argument must be specified to indicate the depth of the break out area from the specified point. 2. A **DrawingSketch** object which is associated with a dependant projected view. 3. A **DrawingCurve** object that is used to specify a 'hole'. A hole in this case is any geometry from a HoleFeature object or any cylinder or cone in the model. The axis of the hole, cylinder, or cone must be parallel to the sheet plane. The axis defines the depth of the hole. 4. A **PartComponentDefinition** object to indicate that the entire part is to be cut. This is only applicable when the drawing view contains a part. The PartComponentDefinition supplied must be the component definition of the part in the view. 5. A **ComponentOccurrence** (or a ComponentOccurrenceProxy) object in the context of the parent drawing view. The depth is defined by the depth of the associated part. This is only applicable when the drawing view contains an assembly. 6. An **ObjectCollection** containing multiple ComponentOccurrence (or ComponentOccurrenceProxy) objects. The depth is defined by the depths of the associated parts. This is only applicable when the drawing view contains an assembly. |
| DepthValue | Double | Optional input Double that specifies the depth value for the break out if the input DepthSource is a point. This argument is ignored if the input source is not a point. |
| SectionAllParts | Boolean | Optional input Boolean that specifies whether to section all parts in the break out area. The default value is False indicating that all parts will not be sectioned.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010
