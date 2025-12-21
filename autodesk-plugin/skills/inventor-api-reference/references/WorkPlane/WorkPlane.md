# WorkPlane Object

## Description

Represents a work plane. See [here](WorkFeatures_Overview.md) for an overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../WorkPlane/WorkPlane_Delete.md) | Method that deletes the work plane. Optionally the dependent objects will be deleted. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [FlipNormal](../WorkPlane/WorkPlane_FlipNormal.md) | Method that reverses the normal of the work plane. The current normal direction can be determined by using the Plane object returned by Plane property of the work plane. |
| [GetPosition](../WorkPlane/WorkPlane_GetPosition.md) | Method that returns the position and orientation of a work plane. When sketches are created on a work plane they inherit the work plane's origin and orientation. This method is useful to predetermine what the orientation will be before the sketch is created. |
| [GetReferenceKey](../WorkPlane/WorkPlane_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSize](../WorkPlane/WorkPlane_GetSize.md) | Method that gets the current size of the displayed graphics for the work plane. The returned points are in the coordinate space of the workplane. |
| [SetByLineAndTangent](../WorkPlane/WorkPlane_SetByLineAndTangent.md) | Method that redefines the work plane to be through the input line and tangent to the input surface. |
| [SetByLinePlaneAndAngle](../WorkPlane/WorkPlane_SetByLinePlaneAndAngle.md) | Method that redefines the work plane to be through the input line at the specified angle from the input plane. |
| [SetByNormalToCurve](../WorkPlane/WorkPlane_SetByNormalToCurve.md) | Method that redefines the work plane to pass through the input point and normal to the input curve. |
| [SetByPlaneAndOffset](../WorkPlane/WorkPlane_SetByPlaneAndOffset.md) | Method that redefines the work plane to be parallel to the input plane at a specified distance in the specified direction. |
| [SetByPlaneAndPoint](../WorkPlane/WorkPlane_SetByPlaneAndPoint.md) | Method that redefines the work plane to be parallel to the input plane and passing through the input point. |
| [SetByPlaneAndTangent](../WorkPlane/WorkPlane_SetByPlaneAndTangent.md) | Method that redefines the work plane to be parallel to the input plane and tangent to the input surface. |
| [SetByPointAndTangent](../WorkPlane/WorkPlane_SetByPointAndTangent.md) | Method that redefines the work plane to pass through the input point and tangent to the input surface. |
| [SetByThreePoints](../WorkPlane/WorkPlane_SetByThreePoints.md) | Method that redefines the work plane to be based on the three input points. |
| [SetByTorusMidPlane](../WorkPlane/WorkPlane_SetByTorusMidPlane.md) | Method that redefines the work plane to be at the mid-plane of the torus specified by the input face. |
| [SetByTwoLines](../WorkPlane/WorkPlane_SetByTwoLines.md) | Method that redefines the work plane to be based on the two input lines. |
| [SetByTwoPlanes](../WorkPlane/WorkPlane_SetByTwoPlanes.md) | Method that redefines a bisection work plane to be based on the two planes. |
| [SetEndOfPart](../WorkPlane/WorkPlane_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SetFixed](../WorkPlane/WorkPlane_SetFixed.md) | Method that redefines the work plane at the position and orientation defined by the point and X and Y axis vectors. |
| [SetSize](../WorkPlane/WorkPlane_SetSize.md) | Method that sets the current size of the displayed graphics for the work plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../WorkPlane/WorkPlane_Adaptive.md) | Specifies whether the work plane is adaptive. |
| [Application](../WorkPlane/WorkPlane_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkPlane/WorkPlane_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoResize](../WorkPlane/WorkPlane_AutoResize.md) | Gets and sets whether this work plane should be resized automatically based on the component size. |
| [Construction](../WorkPlane/WorkPlane_Construction.md) | Boolean property that returns whether the work plane is a construction work plane or not. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. Some properties and methods of the WorkPlane object will behave differently for a construction work plane. These are Adaptive, Name, Visible, GetSize, and SetSize. |
| [Consumed](../WorkPlane/WorkPlane_Consumed.md) | Gets whether the WorkPlane is consumed or not. |
| [ConsumeInputs](../WorkPlane/WorkPlane_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../WorkPlane/WorkPlane_Definition.md) | Property that returns one of the work plane definition objects. Which definition object returned will depend on how the work plane is defined. The DefinitionType property can be used to determine the type of definition the Definition property will return. |
| [DefinitionType](../WorkPlane/WorkPlane_DefinitionType.md) | Property that returns the type of definition that is used to define the work plane. This can be kThreePointsWorkPlane, kTwoLinesWorkPlane, kLineAndPointWorkPlane, kPlaneAndPointWorkPlane, kLinePlaneAndAngleWorkPlane, kPlaneAndOffsetWorkPlane, kLineAndTangentWorkPlane, kPlaneAndTangentWorkPlane, kSketchWorkPlane, kFixedWorkPlane, kNormalToCurveWorkPlane, kTwoPlanesWorkPlane, kTorusMidPlaneWorkPlane, or AssemblyWorkPlane. |
| [Dependents](../WorkPlane/WorkPlane_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the work plane. |
| [DrivenBy](../WorkPlane/WorkPlane_DrivenBy.md) | Property that returns the collection of objects that the work plane is dependent on. |
| [Exported](../WorkPlane/WorkPlane_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Grounded](../WorkPlane/WorkPlane_Grounded.md) | Gets/Sets the Boolean flag that specifies whether this work plane is grounded or not. |
| [HasReferenceComponent](../WorkPlane/WorkPlane_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../WorkPlane/WorkPlane_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsCoordinateSystemElement](../WorkPlane/WorkPlane_IsCoordinateSystemElement.md) | Property that returns whether the work plane belongs to a coordinate system. If so, edits and delete are not allowed. |
| [IsOwnedByFeature](../WorkPlane/WorkPlane_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsParentSketch](../WorkPlane/WorkPlane_IsParentSketch.md) | Property that indicates whether the work plane belongs to a 3d sketch. |
| [IsPatternElement](../WorkPlane/WorkPlane_IsPatternElement.md) | Property that gets whether the work plane was created by a pattern. If so, edits and delete are not allowed. |
| [Name](../WorkPlane/WorkPlane_Name.md) | Specifies the name of the work plane. |
| [OwnedBy](../WorkPlane/WorkPlane_OwnedBy.md) | Read-only property that returns the client feature that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../WorkPlane/WorkPlane_Parent.md) | Property returning the parent  object. |
| [ParentSketch](../WorkPlane/WorkPlane_ParentSketch.md) | Gets the parent 3d sketch if this work plane belongs to a 3d sketch, Gets Nothing otherwise. |
| [Plane](../WorkPlane/WorkPlane_Plane.md) | Property that returns a Plane's geometry. The Plane object returned provides information about the position and normal of the work plane. |
| [ReferenceComponent](../WorkPlane/WorkPlane_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../WorkPlane/WorkPlane_ReferencedEntity.md) | Property that returns the referenced WorkPlane in the case where this work plane was created using a referenced component. An example of this is when a work plane is selected as part of a derived part. The HasReferenceComponent property indicates if this work plane is based on a referenced component or not. This property returns Nothing in the case where it is not based on a referenced component. |
| [Shared](../WorkPlane/WorkPlane_Shared.md) | Gets and sets whether the work plane is shared or not. |
| [Type](../WorkPlane/WorkPlane_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkPlane/WorkPlane_Visible.md) | Specifies the visibility of the work plane. |

## Accessed From

[AssemblyWorkPlaneDef.Parent](../AssemblyWorkPlaneDef/AssemblyWorkPlaneDef_Parent.md), [FixedWorkPlaneDef.Parent](../FixedWorkPlaneDef/FixedWorkPlaneDef_Parent.md), [LineAndPointWorkPlaneDef.Parent](LineAndPointWorkPlaneDef_Parent.md), [LineAndTangentWorkPlaneDef.Parent](../LineAndTangentWorkPlaneDef/LineAndTangentWorkPlaneDef_Parent.md), [LinePlaneAndAngleWorkPlaneDef.Parent](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef_Parent.md), [NormalToCurveWorkPlaneDef.Parent](../NormalToCurveWorkPlaneDef/NormalToCurveWorkPlaneDef_Parent.md), [PlaneAndOffsetWorkPlaneDef.Parent](../PlaneAndOffsetWorkPlaneDef/PlaneAndOffsetWorkPlaneDef_Parent.md), [PlaneAndPointWorkPlaneDef.Parent](../PlaneAndPointWorkPlaneDef/PlaneAndPointWorkPlaneDef_Parent.md), [PlaneAndTangentWorkPlaneDef.Parent](../PlaneAndTangentWorkPlaneDef/PlaneAndTangentWorkPlaneDef_Parent.md), [PointAndTangentWorkPlaneDef.Parent](../PointAndTangentWorkPlaneDef/PointAndTangentWorkPlaneDef_Parent.md), [ThreePointsWorkPlaneDef.Parent](../ThreePointsWorkPlaneDef/ThreePointsWorkPlaneDef_Parent.md), [TorusMidPlaneWorkPlaneDef.Parent](../TorusMidPlaneWorkPlaneDef/TorusMidPlaneWorkPlaneDef_Parent.md), [TwoLinesWorkPlaneDef.Parent](../TwoLinesWorkPlaneDef/TwoLinesWorkPlaneDef_Parent.md), [TwoPlanesWorkPlaneDef.Parent](../TwoPlanesWorkPlaneDef/TwoPlanesWorkPlaneDef_Parent.md), [UserCoordinateSystem.XYPlane](../UserCoordinateSystem/UserCoordinateSystem_XYPlane.md), [UserCoordinateSystem.XZPlane](../UserCoordinateSystem/UserCoordinateSystem_XZPlane.md), [UserCoordinateSystem.YZPlane](../UserCoordinateSystem/UserCoordinateSystem_YZPlane.md), [UserCoordinateSystemProxy.XYPlane](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XYPlane.md), [UserCoordinateSystemProxy.XZPlane](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XZPlane.md), [UserCoordinateSystemProxy.YZPlane](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_YZPlane.md), [WorkPlane.ReferencedEntity](../WorkPlane/WorkPlane_ReferencedEntity.md), [WorkPlaneProxy.NativeObject](../WorkPlaneProxy/WorkPlaneProxy_NativeObject.md), [WorkPlaneProxy.ReferencedEntity](../WorkPlaneProxy/WorkPlaneProxy_ReferencedEntity.md), [WorkPlanes.AddByLineAndTangent](../WorkPlanes/WorkPlanes_AddByLineAndTangent.md), [WorkPlanes.AddByLinePlaneAndAngle](../WorkPlanes/WorkPlanes_AddByLinePlaneAndAngle.md), [WorkPlanes.AddByNormalToCurve](../WorkPlanes/WorkPlanes_AddByNormalToCurve.md), [WorkPlanes.AddByPlaneAndOffset](../WorkPlanes/WorkPlanes_AddByPlaneAndOffset.md), [WorkPlanes.AddByPlaneAndPoint](../WorkPlanes/WorkPlanes_AddByPlaneAndPoint.md), [WorkPlanes.AddByPlaneAndTangent](../WorkPlanes/WorkPlanes_AddByPlaneAndTangent.md), [WorkPlanes.AddByPointAndTangent](../WorkPlanes/WorkPlanes_AddByPointAndTangent.md), [WorkPlanes.AddByThreePoints](../WorkPlanes/WorkPlanes_AddByThreePoints.md), [WorkPlanes.AddByTorusMidPlane](../WorkPlanes/WorkPlanes_AddByTorusMidPlane.md), [WorkPlanes.AddByTwoLines](../WorkPlanes/WorkPlanes_AddByTwoLines.md), [WorkPlanes.AddByTwoPlanes](../WorkPlanes/WorkPlanes_AddByTwoPlanes.md), [WorkPlanes.AddFixed](../WorkPlanes/WorkPlanes_AddFixed.md), [WorkPlanes.Item](../WorkPlanes/WorkPlanes_Item.md)

## Derived Classes

[WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add mate constraint using work planes in parts](../../sample-programs/AssemblyConstraints_AddMateConstraint2_Sample.md) | This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |