# ComponentOccurrenceProxy Object

Derived from: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ChangeRowOfiAssemblyMember](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ChangeRowOfiAssemblyMember.md) | Method that changes the row in the iAssemblyFactory this occurrence references. This method can be used only if the IsiAssemblyMember property returns True. |
| [ChangeRowOfiPartMember](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ChangeRowOfiPartMember.md) | Method that changes the row in the iPartTable this iPartMember represents. This method can be used only if the iPartMember property is True. |
| [CreateGeometryProxy](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_CreateGeometryProxy.md) | Method that creates a proxy object for input object. A proxy object represents another object within the assembly space. Queries made on the proxy object are returned with respect to the assembly space, not the space the real geometry exists in. |
| [Delete](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Delete.md) | Method that deletes the occurrence. This is the equivalent of the user deleting the occurrence interactively. |
| [Delete2](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Delete2.md) | Deletes this component occurrence. |
| [Edit](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Edit.md) | Activates this component occurrence for editing by the end user via the user interface. |
| [ExitEdit](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ExitEdit.md) | Method that causes the component occurrence to return from the edit mode and into the environment specified by the input argument. If the ComponentOccurrence is not currently active (i.e. this is not the same occurrence as returned by AssemblyComponentDefinition.ActiveOccurrence), then this method does nothing. |
| [GetDegreesOfFreedom](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_GetDegreesOfFreedom.md) | Method that returns the available degrees of freedom for the occurrence. |
| [GetDisplayMode](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_GetDisplayMode.md) | Gets the display mode type - default or override. |
| [GetReferenceKey](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Replace](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Replace.md) | Method that replaces the occurrence or all instances of an occurrence with another file. |
| [Replace2](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Replace2.md) | Replaces this component occurrence with another component. Can save replaced component and unset adaptivity. |
| [SetDesignViewRepresentation](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_SetDesignViewRepresentation.md) | Method that sets a design view representation for an assembly occurrence. |
| [SetDisplayMode](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_SetDisplayMode.md) | Sets the display mode and type - default or override. |
| [SetTransformWithoutConstraints](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_SetTransformWithoutConstraints.md) | Method that sets the position and orientation of the occurrence, ignoring any constraints on the occurrence. When the assembly is recomputed the occurrence will reposition to honor the constraints. |
| [ShowRelationships](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ShowRelationships.md) | Method that shows all of the assembly constraints, joints and iMate objects associated with this occurrence. |
| [Suppress](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Suppress.md) | Suppresses this occurrence. |
| [Unsuppress](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Unsuppress.md) | Method that unsuppresses the occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ActiveDesignViewRepresentation.md) | Gets the active Design View Representation for an assembly occurrence. This property returns Nothing in the case where a design view representation was set for the occurrence non-associatively (i.e. with the 'Associative' flag turned off). |
| [ActiveModelState](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ActiveModelState.md) | Read-write property that gets and sets the name of the active model state for an assembly occurrence. |
| [ActivePositionalRepresentation](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ActivePositionalRepresentation.md) | Gets and sets the active Positional Representation for this occurrence. |
| [Adaptive](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Adaptive.md) | 'Put' is Inventor Only: Gets/Sets the Boolean flag that specifies whether this Occurrence is adaptive or not. |
| [Appearance](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Appearance.md) | Gets and sets the current appearance of the component occurrence. |
| [AppearanceSourceType](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the component occurrence. |
| [Application](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssociativeForeignFilename](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_AssociativeForeignFilename.md) | Read-only property that returns the full file name of the associative foreign file. This property returns empty string if the IsAssociativelyImported returns False. |
| [AttributeSets](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BOMStructure](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_BOMStructure.md) | Gets and sets the BOM structure override. |
| [Constraints](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Constraints.md) | Property returns the collection of constraints that are acting on the occurrence. |
| [ContactSet](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ContactSet.md) | Gets and sets whether the component belongs in the contact set. |
| [ContainingOccurrence](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContextDefinition](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ContextDefinition.md) | Property that returns the object this occurrence is in the context of. For example, all coordinate data returned by the definition is in the space of this ComponentDefinition. |
| [Definition](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Definition.md) | Property that returns the object this occurrence references. |
| [DefinitionDocumentType](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_DefinitionDocumentType.md) | Gets the type of the Document whose occurrence this is. |
| [DisabledActionTypes](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_DisabledActionTypes.md) | Gets and sets the action types valid for this component occurrence. |
| [Enabled](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Enabled.md) | 'Put' is Inventor Only: Gets/Sets the Boolean flag that specifies whether this Occurrence is enabled or not. |
| [Excluded](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Excluded.md) | Read-write property that gets and sets whether the occurrence is excluded in the active row of the iAssembly factory. This property returns False and cannot be set to True if the parent document is not an iAssembly. |
| [Flexible](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Flexible.md) | Only works for assembly occurrences. Gets and sets the Boolean flag that specifies whether the assembly is flexible. |
| [Grounded](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Grounded.md) | 'Put' is Inventor Only: Gets/Sets the Boolean flag that specifies whether this Occurrence is grounded or not. |
| [HasAssociativeImportedComponent](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_HasAssociativeImportedComponent.md) | Read-only property that returns whether the ComponentOccurrence has an associative imported component. |
| [HasBodyOverride](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_HasBodyOverride.md) | Property that returns a Boolean specifying whether the occurrence path contains body-modifying assembly features. |
| [iMateDefinitions](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_iMateDefinitions.md) | Property that returns the iMateDefinitions that are available from this occurrence. The iMateDefinition objects returned are actually proxies for the various iMateDefinition objects. These can be used as input to the Add and ValidResult methods of the iMateResults object. |
| [ImportedComponent](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ImportedComponent.md) | Read-only property that returns the associative ImportedComponent object if the HasAssociativeImportedComponent returns True. |
| [IsAssociativelyImported](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_IsAssociativelyImported.md) | Gets whether this occurrence is an associatively imported occurrence. |
| [IsAssociativeToDesignViewRepresentation](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_IsAssociativeToDesignViewRepresentation.md) | Gets and sets whether this occurrence is associative to a design view representation. |
| [IsiAssemblyMember](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_IsiAssemblyMember.md) | Property that returns whether the ComponentOccurrence is an iAssemblyMember. The property returns True if the ComponentOccurrence is an iAssemblyMember. This property always returns False for occurrences of part documents. |
| [IsiPartMember](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_IsiPartMember.md) | Property that specifies if the ComponentOccurence is an iPartMember. The property is True if the ComponentOccurence is an iPartMember. |
| [IsPatternElement](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_IsPatternElement.md) | Property that indicates whether this occurrence represents a pattern element. In the case where this occurrence represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [IsSubstituteOccurrence](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_IsSubstituteOccurrence.md) | Property that returns whether this occurrence references a substitute part in the context of a substitute model state. |
| [Joints](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Joints.md) | Inventor Only: Gets the enumerator that presents the joints applied on this Component Occurrence. |
| [MassProperties](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_MassProperties.md) | Property that returns the MassProperties object. This supports performing mass properties calculations for this particular occurrence. |
| [Name](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Name.md) | Gets/Sets the human-readable name of this Component Occurrence. |
| [NativeObject](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OccurrencePath](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OccurrencePath.md) | Gets the path of immediate (directly instanced) occurrences that make up this occurrence. |
| [OccurrencePropertySets](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OccurrencePropertySets.md) | Read-only property that returns a PropertySets object associated with the occurence. |
| [OccurrencePropertySetsEnabled](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OccurrencePropertySetsEnabled.md) | Read-write property that gets and sets whether this occurrence has a PropertySets object. |
| [OrientedMinimumRangeBox](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [OverrideOpacity](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OverrideOpacity.md) | Gets and sets the opacity of an occurrence. |
| [Parent](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ParentOccurrence](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ParentOccurrence.md) | Property that returns the parent of this occurrence. This property is only valid for the occurrences in a multi-level assembly that are not in the top level. The parent occurrence is the occurrence representing the subassembly this occurrence is contained within. |
| [PatternElement](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_PatternElement.md) | Property that returns the pattern element this occurrence represents. In the case where this occurrence is not part of a pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence is part of a pattern. |
| [PreciseRangeBox](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_PreciseRangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that tightly encloses this object. |
| [RangeBox](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ReferencedDocumentDescriptor](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ReferencedDocumentDescriptor.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ShowDegreesOfFreedom](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ShowDegreesOfFreedom.md) | Gets and sets whether to display the degrees of freedom for the occurrence. |
| [SubOccurrences](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_SubOccurrences.md) | Property that returns the collection of occurrences for an occurrence. This property applies to occurrences that represent a subassembly. The collection returned provides access to the occurrences contained within the subassembly. If this collection is obtained from an occurrence that represents a part, it will not contain any occurrences. |
| [Suppressed](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Suppressed.md) | Property that returns whether this occurrence is suppressed or not. |
| [SurfaceBodies](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_SurfaceBodies.md) | Property that returns the SurfaceBodies collection for the occurrence. This property applies to occurrences that represent a part and provides access to the B-Rep of that part. The B-Rep queries will return coordinate data in the context of the component definition that served as the starting point to access the occurrence, which can also be accessed through the ContextDefinition property. |
| [Transformation](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Transformation.md) | Property that returns and sets the transformation for the occurrence. The transformation matrix defines the position and orientation of the component within the assembly. When setting the transform of an occurrence the actual change in position and orientation of the occurrence is limited by the constraints on the occurrence. |
| [Transparent](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Transparent.md) | 'Put' is Inventor Only: Gets/Sets the Boolean flag that specifies whether this Occurrence is transparent or not. |
| [Type](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_Visible.md) | 'Put' is Inventor Only: Gets/Sets the Boolean flag that specifies whether this Occurrence is visible or not. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Promote occurence](../../sample-programs/BrowserPaneObject_Reorder_Promote_Sample.md) | This sample demonstrates how to promote an occurrence. |
| [Print instance properties of all components in an assembly](../../sample-programs/PrintInstancePropertiesSample_Sample.md) | This sample demonstrates how to get the instance properties of all components in an assembly. |

## Version

Introduced in version 4
