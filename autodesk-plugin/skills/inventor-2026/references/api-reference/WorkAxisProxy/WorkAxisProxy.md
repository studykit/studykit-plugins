# WorkAxisProxy Object

Derived from: [WorkAxis](../WorkAxis/WorkAxis.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../WorkAxisProxy/WorkAxisProxy_Delete.md) | Method that deletes the work axis. Optionally the dependent objects will be deleted. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetReferenceKey](../WorkAxisProxy/WorkAxisProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSize](../WorkAxisProxy/WorkAxisProxy_GetSize.md) | Method that gets the current size of the displayed graphics for the work axis. The returned points are in model coordinate space. |
| [SetByAnalyticEdge](../WorkAxisProxy/WorkAxisProxy_SetByAnalyticEdge.md) | Method that redefines the work axis to be based on the input edge. |
| [SetByLine](../WorkAxisProxy/WorkAxisProxy_SetByLine.md) | Method that redefines the work axis to be based on the input line. This method is not valid when the work axis exists in an Assembly component definition. |
| [SetByLineAndPlane](../WorkAxisProxy/WorkAxisProxy_SetByLineAndPlane.md) | Method that redefines the work axis so that it is along a line defined by projecting the input line onto the input plane along the plane normal. |
| [SetByLineAndPoint](../WorkAxisProxy/WorkAxisProxy_SetByLineAndPoint.md) | Method that redefines the work axis so that it is parallel to a line and passes through the input point. |
| [SetByNormalToSurface](../WorkAxisProxy/WorkAxisProxy_SetByNormalToSurface.md) | Method that redefines the work axis to pass through the input point and be normal to the input surface. |
| [SetByRevolvedFace](../WorkAxisProxy/WorkAxisProxy_SetByRevolvedFace.md) | Method that redefines the work axis to be at the axis of the input revolved face. |
| [SetByTwoPlanes](../WorkAxisProxy/WorkAxisProxy_SetByTwoPlanes.md) | Method that redefines the work axis to be at the intersection of the two input planes. |
| [SetByTwoPoints](../WorkAxisProxy/WorkAxisProxy_SetByTwoPoints.md) | Method that redefines the work axis to go between the two input points. |
| [SetEndOfPart](../WorkAxisProxy/WorkAxisProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SetFixed](../WorkAxisProxy/WorkAxisProxy_SetFixed.md) | Method that redefines the work axis so it passes through the input point in the direction of the input vector. |
| [SetSize](../WorkAxisProxy/WorkAxisProxy_SetSize.md) | Method that sets the current size of the displayed graphics for the work axis. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../WorkAxisProxy/WorkAxisProxy_Adaptive.md) | Specifies whether the work axis is adaptive. |
| [Application](../WorkAxisProxy/WorkAxisProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkAxisProxy/WorkAxisProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoResize](../WorkAxisProxy/WorkAxisProxy_AutoResize.md) | Gets or sets whether this work axis should be resized automatically based on the component size. |
| [Construction](../WorkAxisProxy/WorkAxisProxy_Construction.md) | Boolean property that returns whether the work axis is a construction work axis or not. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. Some properties and methods of the WorkAxis object will behave differently for a construction work axis. These are Adaptive, Name, and Visible. |
| [Consumed](../WorkAxisProxy/WorkAxisProxy_Consumed.md) | Gets whether the WorkAxis is consumed or not. |
| [ConsumeInputs](../WorkAxisProxy/WorkAxisProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../WorkAxisProxy/WorkAxisProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../WorkAxisProxy/WorkAxisProxy_Definition.md) | Property that returns one of the work axis definition objects. Which definition object returned will depend on how the work axis is defined. The DefinitionType property can be used to determine the type of definition the Definition property will return. |
| [DefinitionType](../WorkAxisProxy/WorkAxisProxy_DefinitionType.md) | Property that returns the type of definition that is used to define the work axis. This can be kLineWorkAxis, kTwoPlanesWorkAxis, kTwoPointsWorkAxis, kRevolvedFaceWorkAxis, kNormalToSurfaceWorkAxis, kLineAndPlaneWorkAxis, kLineAndPointWorkAxis, kAnalyticEdgeWorkAxis, kFixedWorkAxis, or kAssemblyWorkAxis. |
| [Dependents](../WorkAxisProxy/WorkAxisProxy_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the work axis. |
| [DrivenBy](../WorkAxisProxy/WorkAxisProxy_DrivenBy.md) | Property that returns the collection of objects that the work axis is dependent on. |
| [Exported](../WorkAxisProxy/WorkAxisProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Grounded](../WorkAxisProxy/WorkAxisProxy_Grounded.md) | Gets/Sets the Boolean flag that specifies whether this work axis is grounded or not. |
| [HasReferenceComponent](../WorkAxisProxy/WorkAxisProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../WorkAxisProxy/WorkAxisProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsCoordinateSystemElement](../WorkAxisProxy/WorkAxisProxy_IsCoordinateSystemElement.md) | Property that returns whether the work axis belongs to a coordinate system. If so, edits and delete are not allowed. |
| [IsOwnedByFeature](../WorkAxisProxy/WorkAxisProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsParentSketch](../WorkAxisProxy/WorkAxisProxy_IsParentSketch.md) | Property that indicates whether the work axis belongs to a 3d sketch. |
| [IsPatternElement](../WorkAxisProxy/WorkAxisProxy_IsPatternElement.md) | Property that gets whether the work axis was created by a pattern. If so, edits and delete are not allowed. |
| [Line](../WorkAxisProxy/WorkAxisProxy_Line.md) | Property that returns a Line geometry. The Line object returned provides information about the position and direction of the work axis. |
| [Name](../WorkAxisProxy/WorkAxisProxy_Name.md) | Specifies the name of the work axis. |
| [NativeObject](../WorkAxisProxy/WorkAxisProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../WorkAxisProxy/WorkAxisProxy_OwnedBy.md) | Read-only property that returns the client feature that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../WorkAxisProxy/WorkAxisProxy_Parent.md) | Property returning the parent  object. |
| [ParentSketch](../WorkAxisProxy/WorkAxisProxy_ParentSketch.md) | Property that returns the parent ComponentDefinition object. |
| [ReferenceComponent](../WorkAxisProxy/WorkAxisProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../WorkAxisProxy/WorkAxisProxy_ReferencedEntity.md) | Property indicating the object this entity is dependent on. |
| [Shared](../WorkAxisProxy/WorkAxisProxy_Shared.md) | Gets and sets whether the work axis is shared or not. |
| [Type](../WorkAxisProxy/WorkAxisProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkAxisProxy/WorkAxisProxy_Visible.md) | Specifies the visibility of the work axis. |

## Version

Introduced in version 5
