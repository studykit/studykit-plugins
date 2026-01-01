# MiniToolbarDropdown.OnPreMenuDisplay Event

Parent Object: [MiniToolbarDropdown](../MiniToolbarDropdown/MiniToolbarDropdown.md)

## Description

Event that is fired when the user clicks the dropdown in a way where the drop down menu will be displayed. The event is fired just before the contents of the drop down list are shown to the user, so you can dynamically modify the contents of the list. If the IsSplitButton property is True, then clicking on the arrow to the right of the button will cause this event to be fired and display the drop-down list. Clicking the button itself is result in the OnSelect event to be fired. If the IsSplitbutton property is False, clicking the button will cause this event to be fired and display the drop-down list.

## Syntax

MiniToolbarDropdown.**OnPreMenuDisplay**()

## Version

Introduced in version 2012
