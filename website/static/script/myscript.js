

function valida_form (){

    if(document.getElementById("estabelecimento").value == ""){
        alert('Por favor, marque o estabelecimento');
        document.getElementById("estabelecimento").focus();
        return false;
    }
    if(document.getElementById("tipo").value == ""){
        alert('Por favor, preencha o campo tipo do item');
        document.getElementById("tipo_item").focus();
        return false;
    }
    if(document.getElementById("nome").value == ""){
        alert('Por favor, preencha o campo nome do produto');
        document.getElementById("nome_item").focus();
        return false;
    }
    if(document.getElementById("marca").value == ""){
        alert('Por favor, preencha o campo marca');
        document.getElementById("marca_item").focus();
        return false;
    }
    if(document.getElementById("quantidade").value == ""){
        alert('Por favor, preencha o campo tipo da quantidade');
        document.getElementById("volume_tipo").focus();
        return false;
    }
    if(document.getElementById("volume").value == ""){
        alert('Por favor, preencha o campo quantidade');
        document.getElementById("volume").focus();
        return false;
    }
    if(document.getElementById("qtd_maxima").value == ""){
        alert('Por favor, preencha o campo quantidade máxima');
        document.getElementById("qtd_maxima").focus();
        return false;
    }
    if(document.getElementById("valor").value == ""){
        alert('Por favor, preencha o campo valor');
        document.getElementById("valor").focus();
        return false;
    }
    if(document.getElementById("foto").value == ""){
        alert('Por favor, preencha adicione uma foto do produto');
        document.getElementById("foto").focus();
        return false;
    }
    if(document.getElementById("data_fim_promocao").value == ""){
        alert('Por favor, preencha o campo data final da promoção');
        document.getElementById("data_fim_promocao").focus();
        return false;
    }
}




function valida_estab(){
    if(document.getElementById("nome").value == ""){
        alert('Por favor, preencha o nome do estabeleimento');
        document.getElementById("nome").focus();
        return false;
    }
    if(document.getElementById("endereco").value == ""){
        alert('Por favor, preencha com endereço do estabelecimento');
        document.getElementById("endereco").focus();
        return false;
    }
    if(document.getElementById("descricao").value == ""){
        alert('Por favor, preencha com uma descrição breve do establecimento');
        document.getElementById("descricao").focus();
        return false;
    }
    if(document.getElementById("telefone").value == ""){
        alert('Por favor, preencha com um contato');
        document.getElementById("telefone").focus();
        return false;
    }
    if(document.getElementById("foto").value == ""){
        alert('Por favor, faça upload da foto da marca/logo fdo estabelicimento');
        document.getElementById("foto").focus();
        return false;
    }
    if(document.getElementById("fotob").value == ""){
        alert('Por favor, faça upload da foto 2 do estabelecimento');
        document.getElementById("fotob").focus();
        return false;
    }
    if(document.getElementById("fotoc").value == ""){
        alert('Por favor, faça upload da foto 3 do estabelecimento');
        document.getElementById("fotoc").focus();
        return false;
    }
    if(document.getElementById("fotod").value == ""){
        alert('Por favor, faça upload da foto 2 do estabelecimento');
        document.getElementById("fotod").focus();
        return false;
    }
    
}