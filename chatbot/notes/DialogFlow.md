### Steps to create minimal chatbot
1. Create Agent - The actual bot
2. To test, go to integrations -> check web integration.
3. To improve, create intents (collection of conversation on a specific topic)
   1. Add training phrases.
   2. Add responses.
        >These two are needed for minimal conversation.
   3. Add Entity (variables extracted during conversation)
      1. Predefined. Eg.
        ![picture 1](../../images/8a9073ad4ad0c92b7a7366fcc061f36a98aacd6519181d1b15dd56c8d5bb8ddd.png)  
       2. Custom. Eg.
        ![picture 2](../../images/46ebca642a5e8cdf564816f816c1627bed68ac29e3ce9466763894f91bc77d6a.png)  
        ![picture 3](../../images/5f5d7166a46738d76b82b4f1b383edfe2dc0e3192672c79317d030faefc83cb3.png)
    >First add entity, then training expressions to avoid some errors.

    >We can make an entity required and add prompt if user doesn't provides it.

#### Small Talk
- [ ] Small Talk section in dialogflow lists out common questions asked to a chatbot (pre-populated by google). You can add the response you wish to add.