# WorkAxis Object

## Description

Represents a work axis. See [here](WorkFeatures_Overview.md) for an overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../WorkAxis/WorkAxis_Delete.md) | Method that deletes the work axis. Optionally the dependent objects will be deleted. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetReferenceKey](../WorkAxis/WorkAxis_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSize](../WorkAxis/WorkAxis_GetSize.md) | Method that gets the current size of the displayed graphics for the work axis. The returned points are in model coordinate space. |
| [SetByAnalyticEdge](../WorkAxis/WorkAxis_SetByAnalyticEdge.md) | Method that redefines the work axis to be based on the input edge. |
| [SetByLine](../WorkAxis/WorkAxis_SetByLine.md) | Method that redefines the work axis to be based on the input line. This method is not valid when the work axis exists in an Assembly component definition. |
| [SetByLineAndPlane](../WorkAxis/WorkAxis_SetByLineAndPlane.md) | Method that redefines the work axis so that it is along a line defined by projecting the input line onto the input plane along the plane normal. |
| [SetByLineAndPoint](../WorkAxis/WorkAxis_SetByLineAndPoint.md) | Method that redefines the work axis so that it is parallel to a line and passes through the input point. |
| [SetByNormalToSurface](../WorkAxis/WorkAxis_SetByNormalToSurface.md) | Method that redefines the work axis to pass through the input point and be normal to the input surface. |
| [SetByRevolvedFace](../WorkAxis/WorkAxis_SetByRevolvedFace.md) | Method that redefines the work axis to be at the axis of the input revolved face. |
| [SetByTwoPlanes](../WorkAxis/WorkAxis_SetByTwoPlanes.md) | Method that redefines the work axis to be at the intersection of the two input planes. |
| [SetByTwoPoints](../WorkAxis/WorkAxis_SetByTwoPoints.md) | Method that redefines the work axis to go between the two input points. |
| [SetEndOfPart](../WorkAxis/WorkAxis_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SetFixed](../WorkAxis/WorkAxis_SetFixed.md) | Method that redefines the work axis so it passes through the input point in the direction of the input vector. |
| [SetSize](../WorkAxis/WorkAxis_SetSize.md) | Method that sets the current size of the displayed graphics for the work axis. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../WorkAxis/WorkAxis_Adaptive.md) | Specifies whether the work axis is adaptive. |
| [Application](../WorkAxis/WorkAxis_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkAxis/WorkAxis_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoResize](../WorkAxis/WorkAxis_AutoResize.md) | Gets or sets whether this work axis should be resized automatically based on the component size. |
| [Construction](../WorkAxis/WorkAxis_Construction.md) | Boolean property that returns whether the work axis is a construction work axis or not. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. Some properties and methods of the WorkAxis object will behave differently for a construction work axis. These are Adaptive, Name, and Visible. |
| [Consumed](../WorkAxis/WorkAxis_Consumed.md) | Gets whether the WorkAxis is consumed or not. |
| [ConsumeInputs](../WorkAxis/WorkAxis_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../WorkAxis/WorkAxis_Definition.md) | Property that returns one of the work axis definition objects. Which definition object returned will depend on how the work axis is defined. The DefinitionType property can be used to determine the type of definition the Definition property will return. |
| [DefinitionType](../WorkAxis/WorkAxis_DefinitionType.md) | Property that returns the type of definition that is used to define the work axis. This can be kLineWorkAxis, kTwoPlanesWorkAxis, kTwoPointsWorkAxis, kRevolvedFaceWorkAxis, kNormalToSurfaceWorkAxis, kLineAndPlaneWorkAxis, kLineAndPointWorkAxis, kAnalyticEdgeWorkAxis, kFixedWorkAxis, or kAssemblyWorkAxis. |
| [Dependents](../WorkAxis/WorkAxis_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the work axis. |
| [DrivenBy](../WorkAxis/WorkAxis_DrivenBy.md) | Property that returns the collection of objects that the work axis is dependent on. |
| [Exported](../WorkAxis/WorkAxis_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Grounded](../WorkAxis/WorkAxis_Grounded.md) | Gets/Sets the Boolean flag that specifies whether this work axis is grounded or not. |
| [HasReferenceComponent](../WorkAxis/WorkAxis_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../WorkAxis/WorkAxis_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsCoordinateSystemElement](../WorkAxis/WorkAxis_IsCoordinateSystemElement.md) | Property that returns whether the work axis belongs to a coordinate system. If so, edits and delete are not allowed. |
| [IsOwnedByFeature](../WorkAxis/WorkAxis_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsParentSketch](../WorkAxis/WorkAxis_IsParentSketch.md) | Property that indicates whether the work axis belongs to a 3d sketch. |
| [IsPatternElement](../WorkAxis/WorkAxis_IsPatternElement.md) | Property that gets whether the work axis was created by a pattern. If so, edits and delete are not allowed. |
| [Line](../WorkAxis/WorkAxis_Line.md) | Property that returns a Line geometry. The Line object returned provides information about the position and direction of the work axis. |
| [Name](../WorkAxis/WorkAxis_Name.md) | Specifies the name of the work axis. |
| [OwnedBy](../WorkAxis/WorkAxis_OwnedBy.md) | Read-only property that returns the client feature that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../WorkAxis/WorkAxis_Parent.md) | Property returning the parent  object. |
| [ParentSketch](../WorkAxis/WorkAxis_ParentSketch.md) | Property that returns the parent ComponentDefinition object. |
| [ReferenceComponent](../WorkAxis/WorkAxis_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../WorkAxis/WorkAxis_ReferencedEntity.md) | Property indicating the object this entity is dependent on. |
| [Shared](../WorkAxis/WorkAxis_Shared.md) | Gets and sets whether the work axis is shared or not. |
| [Type](../WorkAxis/WorkAxis_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkAxis/WorkAxis_Visible.md) | Specifies the visibility of the work axis. |

## Accessed From

[AnalyticEdgeWorkAxisDef.Parent](../AnalyticEdgeWorkAxisDef/AnalyticEdgeWorkAxisDef_Parent.md), [AssemblyWorkAxisDef.Parent](../AssemblyWorkAxisDef/AssemblyWorkAxisDef_Parent.md), [FixedWorkAxisDef.Parent](../FixedWorkAxisDef/FixedWorkAxisDef_Parent.md), [LineAndPlaneWorkAxisDef.Parent](../LineAndPlaneWorkAxisDef/LineAndPlaneWorkAxisDef_Parent.md), [LineAndPointWorkAxisDef.Parent](../LineAndPointWorkAxisDef/LineAndPointWorkAxisDef_Parent.md), [LineWorkAxisDef.Parent](../LineWorkAxisDef/LineWorkAxisDef_Parent.md), [NormalToSurfaceWorkAxisDef.Parent](../NormalToSurfaceWorkAxisDef/NormalToSurfaceWorkAxisDef_Parent.md), [PointAndPlaneWorkAxisDef.Parent](PointAndPlaneWorkAxisDef_Parent.md), [RevolvedFaceWorkAxisDef.Parent](../RevolvedFaceWorkAxisDef/RevolvedFaceWorkAxisDef_Parent.md), [TwoPlanesWorkAxisDef.Parent](../TwoPlanesWorkAxisDef/TwoPlanesWorkAxisDef_Parent.md), [TwoPointsWorkAxisDef.Parent](../TwoPointsWorkAxisDef/TwoPointsWorkAxisDef_Parent.md), [UserCoordinateSystem.XAxis](../UserCoordinateSystem/UserCoordinateSystem_XAxis.md), [UserCoordinateSystem.YAxis](../UserCoordinateSystem/UserCoordinateSystem_YAxis.md), [UserCoordinateSystem.ZAxis](../UserCoordinateSystem/UserCoordinateSystem_ZAxis.md), [UserCoordinateSystemProxy.XAxis](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XAxis.md), [UserCoordinateSystemProxy.YAxis](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_YAxis.md), [UserCoordinateSystemProxy.ZAxis](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_ZAxis.md), [WorkAxes.AddByAnalyticEdge](../WorkAxes/WorkAxes_AddByAnalyticEdge.md), [WorkAxes.AddByLine](../WorkAxes/WorkAxes_AddByLine.md), [WorkAxes.AddByLineAndPlane](../WorkAxes/WorkAxes_AddByLineAndPlane.md), [WorkAxes.AddByLineAndPoint](../WorkAxes/WorkAxes_AddByLineAndPoint.md), [WorkAxes.AddByNormalToSurface](../WorkAxes/WorkAxes_AddByNormalToSurface.md), [WorkAxes.AddByRevolvedFace](../WorkAxes/WorkAxes_AddByRevolvedFace.md), [WorkAxes.AddByTwoPlanes](../WorkAxes/WorkAxes_AddByTwoPlanes.md), [WorkAxes.AddByTwoPoints](../WorkAxes/WorkAxes_AddByTwoPoints.md), [WorkAxes.AddFixed](../WorkAxes/WorkAxes_AddFixed.md), [WorkAxes.Item](../WorkAxes/WorkAxes_Item.md), [WorkAxis.ReferencedEntity](../WorkAxis/WorkAxis_ReferencedEntity.md), [WorkAxisProxy.NativeObject](../WorkAxisProxy/WorkAxisProxy_NativeObject.md), [WorkAxisProxy.ReferencedEntity](../WorkAxisProxy/WorkAxisProxy_ReferencedEntity.md)

## Derived Classes

[WorkAxisProxy](../WorkAxisProxy/WorkAxisProxy.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |